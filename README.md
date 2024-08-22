# Sample FastAPI application

Sample FastAPI application.

## Template

Note that this is a template project. You will need to make changes to this application if you want to make use of it. Please read the [Template readme](TEMPLATE.md) file for more information on what this project does and how to use the template.

## Development setup

1. (Optional) Install Pyenv and the Python version for this project:
```shell
pyenv install
```

2. Create a virtual environment:
```shell
# Note: For POSIX, pyenv can create a named virtual environment which you can use instead.
# For Windows, pyenv-win exists, but doesn't have this feature afaik.

python3 -m venv venv

# Windows
./venv/Scripts/activate

# POSIX
source ./venv/bin/activate
```

3. [Windows] Run the `scripts/dev-setup.bat` script:
```shell
./scripts/dev-setup.bat
```

3. [POSIX] Run the `scripts/dev-setup.sh` shell script using any bash-compatible shell:
```shell
bash ./scripts/dev-setup.sh
```

4. Create a `.env` file from the given example and edit it:
```shell
cp .env.example .env

# Open the new .env file in your favourite editor and make the changes
```

5. Run the dev server using `F5` key in VSCode. You can also use the `dev-launch` shell script:
```shell
# Windows
./scripts/dev-launch.bat

# POSIX
bash ./scripts/dev-launch.sh
```

6. You can also run the cli script:
```shell
sample-fastapi --help
```
