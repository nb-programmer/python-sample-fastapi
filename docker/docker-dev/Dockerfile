# Create Docker image for development purposes

FROM python:3.11.9-slim

LABEL maintainer="Narayan Bandodker <narayanband1356@gmail.com>"

RUN apt-get update -y && \
    apt-get install -y openssl

# Create a non-root user
RUN useradd --create-home appuser
USER appuser

# Add the python scripts to PATH
ENV PATH="/home/appuser/.local/bin:$PATH"

WORKDIR /home/appuser

COPY --chown=appuser . .

RUN pip install --no-compile --no-cache-dir --upgrade . uvicorn

ENTRYPOINT ["python3", "-m", "uvicorn", "--factory", "sample_fastapi:init_app"]
