import os
import yaml

def read_config(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, filename)

    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    # Set default properties if they are not present in the config
    host = config.get("host", "localhost")
    messages_count = config.get("messages_count", 1000)
    probability = config.get("probability", 0.5)
    ex_dlx = config.get("ex_dlx", "ex.dlx.messages")
    queue = config.get("queue", "q.messages")
    queue_dlx = config.get("queue_dlx", "q.dlx.messages")
    TTL = config.get("TTL", 20000)

    return host, messages_count, probability, ex_dlx, queue, queue_dlx, TTL
