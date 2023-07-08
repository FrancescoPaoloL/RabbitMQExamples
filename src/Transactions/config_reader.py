import os
import yaml

def read_config(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, filename)

    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    host = config.get("host", "localhost")
    probability = config.get("probability", 0.5)
    queue = config.get("queue", "transactions_queue")
    
    return host, probability, queue
