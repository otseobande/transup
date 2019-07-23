FROM python:3.7.1

LABEL maintainer="otseobande@gmail.com"

WORKDIR /app

RUN apt-get update && apt-get install -y python3-dev libpulse-dev

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD gunicorn -w 1 -k gthread --thread=2 --log-level DEBUG --bind 0.0.0.0:8000 transup.wsgi
