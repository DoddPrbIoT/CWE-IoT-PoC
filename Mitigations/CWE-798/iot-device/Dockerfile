FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY device.py .

ENV APP_USERNAME=admin
ENV APP_PASSWORD=admin

CMD ["python", "-u", "device.py"]
