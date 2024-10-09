# Create Docker image for production use.
# This docker file installs the app package and dependencies at run-time.
# A pre-built wheel is packaged with the Docker image, and a requirements.txt file
# along with it to install the package. An entrypoint script does the setup.
# You can speed up installation by mounting pip-cache folder (or just /root/.cache).

FROM python:3.11.9-slim

LABEL maintainer="Narayan Bandodker <narayanband1356@gmail.com>"

RUN apt-get update -y && \
    apt-get install -y openssl dumb-init

RUN python3 -m pip install --upgrade pip

WORKDIR /app

# Copy container data files
COPY ./docker-data ./

# Copy entrypoint script
COPY ./entrypoint.sh ./dependencies.sh ./
RUN chmod +x ./entrypoint.sh ./dependencies.sh

ENTRYPOINT ["./entrypoint.sh"]
