FROM python:3.11.1-slim-bullseye

# Set PATH
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Activate the virtual environment
COPY /src .
# CMD . /opt/venv/bin/activate
WORKDIR /src