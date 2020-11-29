# Prometheus External Exporter

Collecting simple Prometheus metrics from a host remotely. 

Useful for ensuring a host is up with the proper ports open when you 
cannot run a regular exporter on the host

**Metrics**
- Host up (ping)
- Ports open (nmap)

Metrics are collected from http://hostname:9100/metrics

**Building/running**

Build and run scripts are in the `./scripts` directory

Environment variables:
- `REFRESH_RATE`: Number of seconds before collecting metrics from host again
- `HOST`: Host to collect metrics from
- `DEBUG` (optional): Display debug information or not. Defaults to false





