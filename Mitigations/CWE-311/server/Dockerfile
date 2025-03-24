FROM python:3.9
WORKDIR /app
COPY server.py ssl.crt ssl.key ./
RUN pip install flask
CMD ["python", "server.py"]
