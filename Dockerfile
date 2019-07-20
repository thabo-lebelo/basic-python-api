FROM ubuntu

RUN apt-get update

RUN apt-get install python -y whatever

RUN apt-get install python-pip -y whatever

RUN pip install flask

RUN pip install flask-cors

ENTRYPOINT FLASK_APP = python my_api.py