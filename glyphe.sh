#!/bin/bash
set -e

VENV="framework_env"
REQUIREMENTS="requirements.txt"

# Environnement
if [ ! -d "$VENV" ]; then
    echo "Creation of the virtual environment..."
    python3 -m venv "$VENV"
fi

# Dépendances
if [ -f "requirements.txt" ]; then
    "$VENV/bin/pip" install -r requirements.txt
fi

sudo "$VENV/bin/python" framework.py
