#!/bin/bash

# Setup the development environment

echo 'Creating "dev" folder...'
mkdir "dev/"

echo 'Installing poetry...'
python3 -m pip install poetry

echo 'Installing requirements (all with dev)...'
poetry install --with dev,test

echo 'Installing pre-commit hook...'
pre-commit install

echo 'Running pre-commit test on all files...'
pre-commit run --all-files
