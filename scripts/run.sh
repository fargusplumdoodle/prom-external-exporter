#!/bin/bash
docker run --rm \
	-e HOST=127.0.0.1 \
	-e REFRESH_RATE=60 \
	-v $(pwd)/src:/src \
	-it -p 9100:9100 hub.sekhnet.ra/prom-external-exporter
