FROM python:3.8-slim

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y gcc curl && rm -rf /var/lib/apt/lists/*
ENV PIP_INSTALL="python -m pip --no-cache-dir install --upgrade"
RUN $PIP_INSTALL insightface==0.2.1

WORKDIR /app
