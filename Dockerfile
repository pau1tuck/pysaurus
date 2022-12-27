FROM python:3.11-slim-bullseye
RUN python3 -m venv /opt/venv
COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install -r requirements.txt
COPY ./src .
WORKDIR /src