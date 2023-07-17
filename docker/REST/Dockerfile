FROM python:3.10.6-alpine

RUN mkdir /REST

WORKDIR /REST

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir --upgrade pip

COPY REST /REST


RUN pip install --no-cache-dir --upgrade -r requirements.txt


