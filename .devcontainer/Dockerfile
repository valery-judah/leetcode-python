FROM python:3.12-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    git build-essential ca-certificates curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces/leetcode-python

# Cache layer for tooling
COPY requirements-dev.txt ./
RUN python -m pip install -U pip && pip install -r requirements-dev.txt

# Optional: if some problems use external libs, also copy and preinstall runtime deps
# COPY requirements.txt ./
# RUN pip install -r requirements.txt
