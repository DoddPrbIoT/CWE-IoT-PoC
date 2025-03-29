FROM python:3.9
WORKDIR /app
COPY server.py .
COPY requirements.txt .
RUN pip install flask
RUN pip install -r requirements.txt
CMD ["python", "server.py"]
