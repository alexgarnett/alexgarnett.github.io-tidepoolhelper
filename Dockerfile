# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.9-slim-buster
FROM python:${PYTHON_VERSION} as base

WORKDIR /opt

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT python tidepool_helper/tidepool_helper.py
