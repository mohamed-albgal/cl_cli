#!/bin/zsh

#acitvate the virtualenv (so the cl module is imported
source ~/Desktop/python/cl/cl_cli/venv/bin/activate

#the first arg is the query param
#the last is the today flag if its either y or n
# the rest should all be numbers, take the first 2 and treat first as minp and second as maxp
python3 ~/Desktop/python/cl/cl_cli/src/cl.py "$@"

#deactivate the virutalenv after completion
deactivate
