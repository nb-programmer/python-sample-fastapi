#!/usr/bin/dumb-init /bin/sh

echo '[Entrypoint] Installing server package requirements...'
python3 -m pip install --upgrade -r ./requirements.txt

echo '[Entrypoint] Installing other dependencies...'
. ./dependencies.sh

echo '[Entrypoint] Starting app server...'
exec python3 -m uvicorn --factory tredex_server:init_app "$@"
