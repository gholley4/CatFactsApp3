FROM python:buster

ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME

RUN pip install -r requirements.txt

COPY . $APP_HOME