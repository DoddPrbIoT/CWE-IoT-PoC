FROM ubuntu:latest

WORKDIR /app
COPY . .

RUN apt-get update -y
RUN apt-get install netcat-traditional

CMD [ "nc","-lvp", "8080" ]

EXPOSE 8080