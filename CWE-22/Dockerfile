FROM python:3.9

WORKDIR /app

COPY app.py /app
COPY configs /app/configs

RUN pip install flask

CMD ["python", "app.py"]
