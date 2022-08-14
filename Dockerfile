FROM python:3.9-slim

ENV chall10secret="Damn these processes!"

WORKDIR app

RUN apt update && \
    apt upgrade -y && \
    apt install -y gcc curl

COPY requirements.txt /app
COPY server /app

RUN pip install -r /app/requirements.txt

USER 1001:1001

EXPOSE 8080
ENTRYPOINT gunicorn -w 32 -b 0.0.0.0:8080 server:app
