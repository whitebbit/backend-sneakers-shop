FROM python:3.11.3-alpine3.18
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /service
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5432 8000 6379 9200 9300 5959 5601 9600 9090
