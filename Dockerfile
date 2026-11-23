FROM python:3.11

# Ensure root certificates are always updated at every container build
# and curl is using the latest version of them
RUN apt update && apt upgrade -y \
  && apt install -y curl ca-certificates \
  && update-ca-certificates \
  && rm -rf /var/lib/apt/lists/*

ENV CURL_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt

COPY . .

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000  --workers 2 --forwarded-allow-ips '*' --access-log
