import yaml
import os

from flask import Flask, Response

from prometheus_client import generate_latest, Gauge
import logging

from exporter import Exporter

CONF_LOCATION = os.environ.get("CONF_LOCATION") or "/src/config.yml"
CONTENT_TYPE_LATEST = str("text/plain; version=0.0.4; charset=utf-8")

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/metrics", methods=["GET"])
def get_data():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


def load_config():
    with open(CONF_LOCATION) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    if "debug" not in data or "refresh_rate" not in data or "hosts" not in data:
        logger.fatal(
            'FATAL: /src/config.yml must contain "debug", "refresh_rate" and "hosts"'
        )
        exit(-1)
    return data


if __name__ == "__main__":
    conf = load_config()
    metrics = {
        "ping": Gauge("ping", "Ping duration in ms", ["host"]),
        "ports": Gauge("ports", "Open ports on host", ["host", "port", "protocol"]),
    }
    for host in conf["hosts"]:
        exporter = Exporter(host, conf["refresh_rate"], metrics)
        exporter.start()

    app.run(debug=conf["debug"], host="0.0.0.0", port=9100)
