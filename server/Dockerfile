FROM python:3.9-alpine

ENV PORT 8000
ENV REDIS_HOST "redis"
ENV REDIS_PORT 6379

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN flask -app migrate db init
RUN flask -app migrate db migrate
RUN flask -app migrate db upgrade

CMD ["python", "main.py"]