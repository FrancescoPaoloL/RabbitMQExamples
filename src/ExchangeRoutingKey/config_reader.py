import os
import yaml

def read_config(filename):
    config_dir = os.path.dirname(__file__)
    file_path = os.path.join(config_dir, filename)
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)

    # Set default properties if they are not present in the config
    consistent_hash_exchange_type = config.get("consistent_hash_exchange_type", "x-consistent-hash")
    host = config.get("host", "127.0.0.1")
    queue_name_1 = config.get("queue_name_1", "q.messages1")
    queue_name_2 = config.get("queue_name_2", "q.messages2")
    exchange_name = config.get("exchange_name", "ex.hash")
    my_routing_key = config.get("my_routing_key", "1")
    nr_messages = config.get("nr_messages", 100000)
    timeout = config.get("timeout", 5)

    return consistent_hash_exchange_type, host, \
           queue_name_1, queue_name_2, \
           exchange_name, my_routing_key, \
           nr_messages, timeout

