FROM python:3.8

WORKDIR /code

RUN pip install google-cloud-spanner

COPY *.py .
