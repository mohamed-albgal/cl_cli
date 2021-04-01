#!/bin/zsh


# this assumes virtualenv is named "venv"

#acitvate the virtualenvj
source ./venv/bin/activate

#quotation marks around the $@ causes retention of user-input quotation marks
python3 ./src/cl.py "$@"

#deactivate the virutalenv after completion
deactivate
