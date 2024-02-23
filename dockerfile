FROM python:3.11

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .