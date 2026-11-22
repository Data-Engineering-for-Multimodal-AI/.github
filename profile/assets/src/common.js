const MODS = {
  image: { name: "Image", glyph: '<rect x="3.5" y="5" width="17" height="14" rx="3.5"/><circle cx="9" cy="10" r="1.8"/><path d="M5 17l4.5-4.5 3 3L15 12l4 4"/>' },
  text: { name: "Text", glyph: '<path d="M5 7h14M5 11h14M5 15h9M5 19h6"/>' },
  video: { name: "Video", glyph: '<rect x="3.5" y="6" width="12.5" height="12" rx="3"/><path d="M16 10.5l4.5-2.5v8l-4.5-2.5z"/>' },
  table: { name: "Table", glyph: '<rect x="4" y="5" width="16" height="14" rx="3"/><path d="M4 10h16M4 14.5h16M10 10v9"/>' },
};
const glyph = (m, ink, size = 24) => `<svg width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="${ink}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${MODS[m].glyph}</svg>`;
function squirrel(size = 30, body = "#f2a593", belly = "#fde0d8", ink = "#2a1f1d") {
  return `<svg width="${size}" height="${size}" viewBox="0 0 64 64" role="img" aria-label="The Playbooks squirrel mark">
    <ellipse cx="15" cy="55" rx="9" ry="4" fill="${body}" transform="rotate(-18 15 55)"/>
    <ellipse cx="30" cy="40" rx="15" ry="19" fill="${body}"/>
    <ellipse cx="34" cy="42" rx="8.5" ry="14" fill="${belly}"/>
    <circle cx="34" cy="17" r="11.5" fill="${body}"/>
    <ellipse cx="43.5" cy="19.5" rx="5.5" ry="4.6" fill="${body}"/>
    <circle cx="29.5" cy="7.8" r="3.2" fill="${body}"/>
    <circle cx="29.5" cy="7.8" r="1.5" fill="${belly}"/>
    <circle cx="38.6" cy="15.2" r="1.9" fill="${ink}"/>
    <circle cx="47.6" cy="18.2" r="1.3" fill="${ink}"/>
    <ellipse cx="41" cy="33" rx="4.2" ry="2.6" fill="${body}" transform="rotate(-25 41 33)"/>
    <ellipse cx="34" cy="58" rx="9" ry="3.4" fill="${body}"/>
  </svg>`;
}
