# OpenTelemetry Workshop - Local Copy

To start clone the repo and run:

#### Basic docker-compose commands
```sh
# Re-Build all docker images 
docker-compose build
#  Setup all services
docker-compose up
```

#### Fibo Endpoints
Simple hello world:

```http://localhost:5001/```

Fibonacci's calculation. The `i` is the index from fix series to return
```http request
http://localhost:5001/fib?i=5
```

## Observability Tools
[Jaeger UI](http://localhost:16686/)

[Jaeger Grafana](http://localhost:3000/)