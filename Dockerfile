##### Stage 'base' - Base image #####
FROM python:3.12.2-slim AS base

# Update Ubuntu repos and install required dependencies
RUN apt-get update -y && \
    apt-get install -y openssl && \
    python3 -m pip install --upgrade pip


##### Stage 'builder' - Build wheel #####
FROM base AS builder

ENV POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

ENV PATH="${PATH}:${POETRY_HOME}/bin"

# Create directory for build artifacts
RUN mkdir -p /build

# Install poetry
ADD https://install.python-poetry.org install_poetry.py
RUN python3 install_poetry.py

# Copy source code
WORKDIR /app/src
COPY . .

# Create a blank Readme file for poetry build
RUN touch README.md

# Build package wheel
RUN poetry check && \
    poetry build -f wheel -o /build/dist/

##### Stage 'server' - Build application #####
FROM base AS server

LABEL maintainer="Narayan Bandodker <narayanband1356@gmail.com>"

# Install dumb-init and cURL
RUN apt-get install -y dumb-init curl

WORKDIR /app

# Copy build files from previous stage
COPY --from=builder /build .

# Copy entrypoint script
COPY ./docker-scripts/entrypoint.sh ./docker-scripts/dependencies.sh ./docker-scripts/requirements.txt ./
RUN chmod +x ./entrypoint.sh ./dependencies.sh

ENTRYPOINT ["./entrypoint.sh"]

HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=20 CMD curl --include --request GET http://localhost:8000/health || exit 1
