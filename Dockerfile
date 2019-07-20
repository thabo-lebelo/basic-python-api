FROM ubuntu

RUN apt-get update

RUN apt-get install python -y

RUN apt-get install python-pip -y

RUN pip install flask

RUN pip install flask-cors

ENTRYPOINT FLASK_APP = python my_api.py