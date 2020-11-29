# Prometheus External Exporter

Collecting simple Prometheus metrics from a host remotely. 

Useful for ensuring a host is up with the proper ports open when you 
cannot run a regular exporter on the host

**Metrics**
- Host up (ping)
- Ports open (nmap)

Metrics are available from http://hostname:9100/metrics

**Building/running**

Build and run scripts are in the `./scripts` directory

**Configuring**

edit `./src/config.yml`

Example: 
```yaml
debug: false
refresh_rate: 120  # seconds before scanning hosts again
hosts:  # list of hosts to gather metrics on
- localhost
```

**Helm**

The service is not going to be externally available.  It should be deployed in the same namespace as 
Prometheus.
