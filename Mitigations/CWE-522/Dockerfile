# Base image
FROM python:3.9

WORKDIR /app

COPY app/ /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "server.py"]
