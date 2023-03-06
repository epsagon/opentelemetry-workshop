FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

ENV OTEL_TRACES_EXPORTER=otlp
ENV OTEL_METRICS_EXPORTER=otlp
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317

# Metrics Temporality
ENV OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=cumulative

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Installing Opentelemetry Auto Instrumentation
RUN opentelemetry-bootstrap --action=install

EXPOSE 5002

COPY . .
CMD ["opentelemetry-instrument", "python", "./server.py"]
