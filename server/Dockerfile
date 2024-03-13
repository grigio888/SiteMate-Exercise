FROM python:3.9-alpine

ENV PORT 8000
ENV REDIS_HOST "redis"
ENV REDIS_PORT 6379

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt