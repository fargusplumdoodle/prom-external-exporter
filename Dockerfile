FROM python:latest

ADD ./src /src
WORKDIR /src

RUN apt update && apt install -y nmap
RUN pip install -r requirements.txt

EXPOSE 9100

CMD python app.py

