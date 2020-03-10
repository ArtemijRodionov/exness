FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/code

COPY requirements.txt .
RUN apk update \
    && pip install -r requirements.txt \
    && adduser -D test_assignment
USER test_assignment

COPY . .
CMD ./run.sh

