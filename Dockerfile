FROM python:3.12.1

WORKDIR /app

ARG DB_CERTIFICATE
ENV DB_CERTIFICATE=$DB_CERTIFICATE

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "source/main.py"]
