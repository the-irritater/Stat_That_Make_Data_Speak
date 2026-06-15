#!/bin/bash
set -e

INSTALL_DEPS=false

# Parse arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --install-deps) INSTALL_DEPS=true ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# Check prerequisites
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed or not in PATH."
    exit 1
fi

if ! command -v make &> /dev/null; then
    echo "Error: make is not installed or not in PATH."
    exit 1
fi

if [ "$INSTALL_DEPS" = true ]; then
    echo "Setting up virtual environment and installing dependencies..."
    make setup
else
    echo "Creating virtual environment without installing dependencies..."
    python3 -m venv .venv
    echo "Virtual environment created at .venv."
    echo "To install all dependencies, run: ./setup.sh --install-deps"
fi
