#!/bin/bash

#bold
echo -e "\e[1mbold\e[0m"

#italic
echo -e "\e[3mitalic\e[0m"

# bold italic
echo -e "\e[3m\e[1mbold italic\e[0m"

# underline
echo -e "\e[4munderline\e[0m"

# strikethrough
echo -e "\e[9mstrikethrough\e[0m"

echo "$(tput setaf 0)"black text")(tput sgr0)"
echo "$(tput setaf 1)"red text")(tput sgr0)"
echo "$(tput setaf 2)"green text")(tput sgr0)"
echo "$(tput setaf 3)"yellow text")(tput sgr0)"
echo "$(tput setaf 4)"blue text")(tput sgr0)"
echo "$(tput setaf 5)"magenta text")(tput sgr0)"
echo "$(tput setaf 6)"cyan text")(tput sgr0)"
echo "$(tput setaf 7)"white text")(tput sgr0)"