#!/bin/bash

FILE="requirements.txt"
VENV="django_venv"

python3 -m venv "$VENV"
source "$VENV"/bin/activate

if [ -f "$FILE" ]; then
    pip install -r "$FILE"
else
    echo "'$FILE' not found."
fi
