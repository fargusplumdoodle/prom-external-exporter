#!/bin/bash
helm uninstall prom-external-exporter -n monitoring
helm install prod . \
	--set conf.refresh_rate=600 \
	--set conf.hosts[0]=127.0.0.1 \
	 -n monitoring
