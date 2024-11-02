# Sample FastAPI application

Sample FastAPI application.

## Template

Note that this is a template project. You will need to make changes to this application if you want to make use of it. Please read the [Template readme](TEMPLATE.md) file for more information on what this project does and how to use the template.

## Development setup

### Prerequisites

1. (Optional) Install Pyenv ([Linux](https://github.com/pyenv/pyenv), [Windows](https://github.com/pyenv-win/pyenv-win)) and the [Python installation](.python-version) needed for this project:
```shell
pyenv install
```

2. [Install poetry](https://python-poetry.org/) to your system by following the [setup instructions](https://python-poetry.org/docs/#installation) convenient for you.

> [!IMPORTANT]
> You should **NOT** install poetry into your virtual environment as stated in their docs, as this may mess with your dependencies.

### Setup

1. Create a virtual environment:
```shell
# Note: For POSIX, pyenv can create a named virtual environment which you can use instead.
# For Windows, pyenv-win exists, but doesn't have this feature afaik.

# Create a local virtual environment (inside .venv/)
python3 -m venv .venv

# Activate it:

# Windows
./.venv/Scripts/activate

# POSIX
source ./.venv/bin/activate
```

2. Create development environment and install dependencies (pre-made script does it):

```shell
# [Windows] Run the `scripts/dev-setup.bat` script:
./scripts/dev-setup.bat

# [POSIX] Run the `scripts/dev-setup.sh` shell script using any bash-compatible shell:
bash ./scripts/dev-setup.sh
```

> [!NOTE]
> This scripts does the following:
> Creates a `dev/` folder needed to save log files and other persistent files used by the app, installs the requirements of the app using poetry, installs `pre-commit` hooks to this repository and also runs the pre-commit hooks.

3. Create a `.env` file from the given example and edit it:
```shell
cp .env.example .env

# Open the new .env file in your favourite editor and make the required changes
```

4. Run the dev server using `F5` key in VSCode. You can also use the `dev-launch` shell script:
```shell
# Windows
./scripts/dev-launch.bat

# POSIX
bash ./scripts/dev-launch.sh
```

5. You can also run the cli script:
```shell
sample-fastapi --help
```
