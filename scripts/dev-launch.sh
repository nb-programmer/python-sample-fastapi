#!/bin/bash

# Launch development server

python3 -m uvicorn --factory --reload --host=0.0.0.0 --log-config=config/debug-logger.yml --timeout-graceful-shutdown=10 sample_fastapi:init_app
