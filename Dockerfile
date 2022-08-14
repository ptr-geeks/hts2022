FROM python:3.9-alpine

WORKDIR app

COPY requirements.txt /app
COPY server /app

RUN pip install -r /app/requirements.txt

EXPOSE 8080
ENTRYPOINT gunicorn -w 32 -b 0.0.0.0:8080 server:app
