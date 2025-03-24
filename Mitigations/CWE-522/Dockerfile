# Base image
FROM python:3.9

WORKDIR /app

COPY app/ /app/

RUN pip install -r requirements.txt

ENV API_USERNAME=admin
ENV API_PASSWORD=admin


EXPOSE 5000

CMD ["python", "server.py"]
