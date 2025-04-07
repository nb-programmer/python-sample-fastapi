#!/usr/bin/dumb-init /bin/sh

echo '[Entrypoint] Installing server package requirements...'
python3 -m pip install --find-links ./dist/ --upgrade -r ./requirements.txt

echo '[Entrypoint] Installing other dependencies...'
. ./dependencies.sh

echo '[Entrypoint] Starting app server...'
exec python3 -m uvicorn --factory sample_fastapi:init_app "$@"
