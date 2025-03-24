FROM ubuntu:latest

WORKDIR /app
COPY . .

RUN apt-get update -y
RUN apt-get install gcc -y


RUN gcc client.c -o client

CMD [ "./client", "127.0.0.1", "8080" ]