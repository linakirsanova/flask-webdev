#!/bin/bash

# Simple Flask environment setup script
# Usage: source setup_flask_env.sh

# Set Flask environment variables
export FLASK_APP=ragtime.py
export FLASK_DEBUG=1
export FLASK_CONFIG=development

echo "Flask environment variables set:"
echo "FLASK_APP=$FLASK_APP"
echo "FLASK_DEBUG=$FLASK_DEBUG"
echo "FLASK_CONFIG=$FLASK_CONFIG"

echo -e "\nTo use these variables, run this script using 'source':"
echo "    source $(basename "$0")"
echo "or"
echo "    . $(basename "$0")"
