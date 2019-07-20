FROM ubuntu

RUN apt-get update

RUN apt-get install python -y

RUN apt-get install python-pip -y

RUN pip install flask

RUN pip install flask-cors

COPY my_api.py /my_api.py

ENTRYPOINT python my_api.py