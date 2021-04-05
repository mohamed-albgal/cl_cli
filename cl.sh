#!/bin/zsh


# this assumes virtualenv is named "venv"

#acitvate the virtualenvj
. ~/Desktop/python/cl/cl_cli/venv/bin/activate

#quotation marks around the $@ causes retention of user-input quotation marks
python3 ~/Desktop/python/cl/cl_cli/src/cl.py "$@"

#deactivate the virutalenv after completion
deactivate
