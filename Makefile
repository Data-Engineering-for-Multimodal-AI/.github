.PHONY: card

# Make a completion card from the playbooks you finished.
# Usage: make card                 (asks for your name, looks next to this folder)
#        make card NAME="Ada" DIR=~/code
card:
	uv run --no-project --with "pillow>=10.1" python card/card.py $(if $(NAME),--name "$(NAME)") $(if $(DIR),--dir "$(DIR)")
