# temperature_monitor.py

import logging

logging.basicConfig(
    filename="temperature.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

ALERT_THRESHOLD = 80

def check_temperature(temp):
    if temp is None:
        logging.error("Received invalid temperature input: None")
        return "ERROR"

    logging.info(f"Received temperature value: {temp}")

    if temp > ALERT_THRESHOLD:
        logging.warning("Temperature crossed alert threshold")
        return "ALERT"
    else:
        return "NORMAL"
