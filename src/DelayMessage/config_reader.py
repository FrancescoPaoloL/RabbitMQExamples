import os
import yaml

def read_config(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, filename)

    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    # Set default properties if they are not present in the config
    delay_ms = config.get("messages_count", 5000)
    start_datetime = config.get("start_datetime", "0001-01-01 00:00:00")
    expiration_ms = config.get("probability", 20000)
    delayed_exchange = config.get("delayed_exchange", "delayed_exchange")
    delayed_queue = config.get("queue", "delayed_queue")

    return delay_ms, start_datetime, expiration_ms, delayed_exchange, delayed_queue
