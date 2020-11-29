import os

from flask import Flask, Response

from prometheus_client import generate_latest
import logging

from exporter import Exporter

CONTENT_TYPE_LATEST = str("text/plain; version=0.0.4; charset=utf-8")
logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/metrics", methods=["GET"])
def get_data():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    try:
        HOST = os.environ["HOST"]
        REFRESH_RATE = os.environ["REFRESH_RATE"]
    except KeyError:
        logger.fatal(
            'FATAL: Must set "HOST" and "REFRESH_RATE" environment variables. Optionally set "DEBUG"'
        )
        exit(-1)

    exporter = Exporter(HOST, REFRESH_RATE)
    exporter.start()

    app.run(debug=os.environ.get("DEBUG") or False, host="0.0.0.0", port=9100)
