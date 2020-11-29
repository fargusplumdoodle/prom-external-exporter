FROM python:latest

ADD ./src /src
WORKDIR /src

RUN pip install -r requirements.txt
RUN apt update && apt install -y nmap

EXPOSE 9100

CMD python app.py

