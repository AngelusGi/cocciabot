FROM python:3.11-alpine AS build

ARG TG_BOT_TOKEN

RUN pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY ./src .

RUN adduser -D tgbot && \
    chown -R tgbot /app

RUN pip install wheel setuptools && \
    pip install --no-cache-dir --no-clean -r requirements.txt && \
    rm requirements.txt

USER tgbot

CMD ["python", "./main.py"]
