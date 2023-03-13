FROM python:3.7-alpine
WORKDIR /code

RUN apk add --no-cache gcc musl-dev linux-headers g++

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Installing Opentelemetry Auto Instrumentation
RUN opentelemetry-bootstrap --action=install

EXPOSE 5002

COPY . .
CMD ["python", "./server.py"]
