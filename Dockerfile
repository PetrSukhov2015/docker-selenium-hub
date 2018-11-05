FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install -y selenium
