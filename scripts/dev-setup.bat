@REM Setup the development environment

@echo off

echo Creating "dev" folder...
mkdir "dev/"

echo Installing poetry...
python3 -m pip install -q poetry

echo Installing requirements (all with dev)...
poetry -q install --with dev,test

echo Installing pre-commit hook...
pre-commit install

echo Running pre-commit test on all files...
pre-commit run --all-files

echo Running unit tests...
python3 -m unittest
