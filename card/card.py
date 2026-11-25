"""Render a completion card from the playbooks you have finished.

Each playbook writes a `.playbook-done` file in its folder when `make run`
passes. This script looks for those files next to this repository (or in
--dir), counts the chapter playbooks you finished, and draws a PNG.

It runs locally. Nothing is sent anywhere.
"""

import argparse
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent
FONT = HERE / "fonts" / "PlusJakartaSans[wght].ttf"
BOOK = "Data Engineering for Multimodal AI (O'Reilly, 2026)"
CHAPTERS = 12

BG = "#fdfbfa"
INK = "#1f1a19"
MUTED = "#6b6361"
EDGE = "#efe8e6"
CORAL = "#ff9f8e"
CORAL_SOFT = "#ffe8e3"
CORAL_INK = "#b4422e"
ON_CORAL = "#3a1a14"

W, H = 1200, 630
NAME_RE = re.compile(r"playbook-(\d\d)(-bonus)?-")


def find_done(root: Path) -> set[str]:
    """Return the repository names that have a .playbook-done marker."""
    done = set()
    for marker in list(root.glob("*/.playbook-done")) + list(root.glob("*/*/.playbook-done")):
        try:
            first = marker.read_text().splitlines()[0].strip()
        except (OSError, IndexError):
            continue
        if NAME_RE.match(first):
            done.add(first)
    return done


def font(size: int, weight: int) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(FONT), size)
    f.set_variation_by_axes([weight])
    return f


def fit(text: str, size: int, weight: int, width: int) -> ImageFont.FreeTypeFont:
    """Shrink the font until the text fits the width."""
    while size > 24:
        f = font(size, weight)
        if f.getlength(text) <= width:
            return f
        size -= 4
    return font(size, weight)


def draw_card(name: str, done: set[str], out: Path) -> None:
    chapters = sorted({int(m.group(1)) for r in done if (m := NAME_RE.match(r)) and not m.group(2) and m.group(1) != "00"})
    extras = sum(1 for r in done if (m := NAME_RE.match(r)) and (m.group(2) or m.group(1) == "00"))

    img = Image.new("RGB", (W, H), BG)

    # soft coral glow, top left and bottom right
    for box, color, alpha in (((-260, -300, 560, 300), (255, 170, 150), 110), ((820, 460, 1500, 900), (255, 190, 175), 70)):
        mask = Image.new("L", (W, H), 0)
        ImageDraw.Draw(mask).ellipse(box, fill=alpha)
        img.paste(Image.new("RGB", (W, H), color), (0, 0), mask.filter(ImageFilter.GaussianBlur(120)))

    d = ImageDraw.Draw(img)
    x = 80

    # pill
    pill = font(24, 700)
    label = "Completed"
    pw = pill.getlength(label) + 44
    d.rounded_rectangle((x, 72, x + pw, 72 + 48), radius=24, fill=CORAL_SOFT)
    d.text((x + 22, 72 + 24), label, font=pill, fill=CORAL_INK, anchor="lm")

    # name and count
    d.text((x, 160), name, font=fit(name, 76, 800, W - 2 * x), fill=INK)
    count = f"{len(chapters)} of {CHAPTERS} chapter playbooks"
    if extras:
        count += f", plus {extras} starter or bonus"
    d.text((x, 262), count, font=font(34, 600), fill=MUTED)

    # one square per chapter
    size, gap, top = 68, 18, 350
    num = font(26, 700)
    for i in range(1, CHAPTERS + 1):
        left = x + (i - 1) * (size + gap)
        box = (left, top, left + size, top + size)
        if i in chapters:
            d.rounded_rectangle(box, radius=16, fill=CORAL)
            d.text((left + size / 2, top + size / 2), f"{i:02d}", font=num, fill=ON_CORAL, anchor="mm")
        else:
            d.rounded_rectangle(box, radius=16, outline=EDGE, width=3, fill=BG)
            d.text((left + size / 2, top + size / 2), f"{i:02d}", font=num, fill="#cbbfbc", anchor="mm")

    # footer
    foot = font(24, 700)
    d.text((x, H - 72), "The Playbooks", font=foot, fill=INK, anchor="ls")
    d.text((W - x, H - 72), BOOK, font=font(24, 600), fill=MUTED, anchor="rs")

    img.save(out)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--name", help="the name to put on the card")
    p.add_argument("--dir", default=str(HERE.parent.parent), help="folder that holds your playbook clones")
    p.add_argument("--out", default="completion-card.png")
    a = p.parse_args()

    root = Path(a.dir).expanduser().resolve()
    done = find_done(root)
    if not done:
        print(f"No finished playbooks found in {root}.")
        print("Run `make run` in a playbook first, or point to your clones with DIR=/path/to/folder.")
        return 1

    name = a.name or input("Your name for the card: ").strip()
    if not name:
        print("A name is needed for the card.")
        return 1

    out = Path(a.out).resolve()
    draw_card(name, done, out)
    for r in sorted(done):
        print(f"  done: {r}")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
