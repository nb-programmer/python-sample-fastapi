# Sample FastAPI application

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

5. Run the dev server using `F5` key in VSCode.You can also run the server script:
```shell
sample-fastapi --help
```
