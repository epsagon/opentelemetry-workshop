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

## Steps

1. Run the application and access the fib server (via explorer)
   and access fib endpoints.
2. Manual instrumentation!
   1. Manually create a span named “root” in the root handler
   2. Use Console Exporter and see your spans printed to the app console
   3. What you should see?
       1. Browse root
       2. Your span should be visible in the logs
   4. Hint - Use the docs! `opentelemetry.io/docs/instrumentation/python/manual`
3. Send the data to the OTel collector
   1. In your application, add new otlp(gRPC exporter) and send the data to your OTel collector
      1. Make sure you are able to see the spans in the OTel collector logs
4. In the collector, export you traces to zipkin(port 9411), jaeger(port 14250)
   1. You are now should be able to see the spans at: `http://localhost:9411`, `http://localhost:14250`
5. Auto Instrumentation!
   1. In your app, configure Flask auto-instrumentation 
   2. Access to server at `/fib?i=<number>`.
   3. Refresh Zipkin and make sure you can see your Auto instrumentation spans in zipkin
   4. Hint: `Google: “OpenTelemetry flask instrumentation python”`
6. From the collector, exporter traces to Telescope!
   1. Open new account and follow Telescope docs.
7. Add metrics!
   1. In the collector, remove the traces logging exporter (so it won't spam your console)
   2. In the collector, add metrics logging exporter, promethues metrics exporter
   3. Add metrics provider, exporter, etc... and send the data to the collector
   4. Access to Grafana (Which are already connected to prometheus DB) at `http://localhost:3000`
      and make sure you can see metrics.
8. You are new OpenTelemetry professional! :)