FROM python:3.12.1

WORKDIR /app

COPY certs/ca.pem /etc/ssl/certs/ca.pem

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "source/main.py"]
