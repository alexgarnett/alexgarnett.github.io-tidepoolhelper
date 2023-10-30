# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.9-slim-buster
FROM python:${PYTHON_VERSION} as base

WORKDIR /opt

# Copy the source code into the container.
COPY . .

RUN pip install -r requirements.txt

# Expose the port that the application listens on.
#EXPOSE 80

# Run the application.
#CMD flask --app tidepool_helper/tidepool_helper.py run
ENTRYPOINT python tidepool_helper/tidepool_helper.py
