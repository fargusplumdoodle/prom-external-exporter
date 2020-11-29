import logging
import threading
import time
import nmap3

import pythonping


class Exporter(threading.Thread):
    def __init__(self, host, refresh_rate, metrics):
        threading.Thread.__init__(self)
        self.host = host
        self.refresh_rate = refresh_rate
        self.nmap = nmap3.Nmap()
        self.metrics = metrics
        self.logger = logging.getLogger(f"exporter:{self.host}")

    def get_avg_ping_time(self):
        """
        Gets the average ping time.

        Times out at 2000.
        """
        stats = pythonping.ping(self.host)
        ping_durations = [x.time_elapsed_ms for x in stats]

        avg_duration = sum(ping_durations) / len(ping_durations)
        self.logger.debug("Average ping duration: %s", avg_duration)
        self.metrics["ping"].labels(host=self.host).set(avg_duration)

    def get_port_scan(self):
        """
        Gets the open ports on the host

        If the host is down, will return nothing
        """
        self.logger.debug("Starting nmap scan")
        results = self.nmap.nmap_version_detection(self.host)
        self.logger.debug("Finished nmap scan")

        for port in results:
            self.metrics["ports"].labels(
                host=self.host, port=port["port"], protocol=port["protocol"]
            ).set(1)

    def run(self):
        while True:
            self.get_avg_ping_time()
            self.get_port_scan()
            time.sleep(self.refresh_rate)
