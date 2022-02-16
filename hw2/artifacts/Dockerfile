FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y software-properties-common
RUN apt-get install -y pip
RUN apt-get install -y texlive-full

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r /app/requirements.txt

CMD ["python3", "/app/hw2/middle.py"]

