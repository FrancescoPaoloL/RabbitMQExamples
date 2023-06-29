import time
import yaml
import os
from config_reader import read_config
from connection import establish_connection
from queues import declare_queues
from exchange import declare_exchange, bind_queues_to_exchange
from publish import publish_messages, wait_for_confirmation


def main():
    consistent_hash_exchange_type, host, \
    queue_name_1, queue_name_2, \
    exchange_name, my_routing_key, \
    nr_messages, timeout = read_config("config.yaml")

    connection = establish_connection(host)
    with connection:
        channel = connection.channel()

        declare_queues(channel, [queue_name_1, queue_name_2])
        declare_exchange(channel, exchange_name, consistent_hash_exchange_type)
        bind_queues_to_exchange(channel, exchange_name, my_routing_key, [queue_name_1, queue_name_2])

        channel.confirm_delivery()

        delivery_tags = publish_messages(channel, exchange_name, nr_messages)

        wait_for_confirmation(channel, delivery_tags)

        print("Done publishing!")
        print("Evaluating results...")
        time.sleep(timeout)
        print("Done.")

if __name__ == "__main__":
    main()
