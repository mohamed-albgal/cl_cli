#!/bin/zsh

#acitvate the virtualenv (so the cl module is imported
source ~/Desktop/python/cl/cl_cli/venv/bin/activate

#the first arg is the query param
#quotation marks around the $@ causes retention of user-input quotation marks
python3 ~/Desktop/python/cl/cl_cli/src/cl.py "$@"

#deactivate the virutalenv after completion
deactivate
