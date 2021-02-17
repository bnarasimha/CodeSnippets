FROM python:3.8

RUN mkdir /codesnippets

WORKDIR /codesnippets

ADD . /codesnippets/

RUN pip install -r requirements.txt