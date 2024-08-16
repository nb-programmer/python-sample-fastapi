# Template repository

This repository contains a sample Python project for a web application server based on FastAPI.
The project is called `sample-fastapi` and the package is called `sample_fastapi`.

If you want to use this template, you will need to rename the package name and project name occurrences to your project name. A good place to start is the `pyproject.toml` file.

## Features

This Application implements the following:

- A package-hierarchy based FastAPI app that can be installed as a package
- Most common configuration files (.gitignore, .dockerignore, pre-commit, .editorconfig, etc.)
- Should work on Windows and POSIX (Linux, macOS, etc.) systems (not tested)
- FastAPI factory function (`sample_fastapi.init_app()`) to initialize the application and run using `uvicorn`
- App configured with logging and a sample logging config `.yml` for debugging purposes.
    - The debug logger config will create a rotating log file for the root logger, application package and uvicorn and store them in the `dev/` folder. It also has console handlers.
    - Note: Your deployment folder will contain a mount folder with similar config files.
- Sample routes inside `resources/`:
    - Hello world
    - Calculator / Converter
- Test suite:
    - Sample test cases in `unittest` for testing the application and its resources.
    - VSCode config for detecting the test suite
- Pre-commit config script
    - Some preset repos like flake8, isort, codespell, etc.
    - Also has some of its tools' configuration in the `pyproject.toml` file.
- Development setup script to quickly install all dependencies needed.
- A `.env.example` configuration example that needs to be cloned into `.env`
- Examples (Only Docker script for now)
