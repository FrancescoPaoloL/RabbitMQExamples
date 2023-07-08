import pika
import random
from consume import consume_messages
from config_reader import read_config

def send_messages(messages_count, probability, ex_dlx, queue, queue_dlx, TTL):
    messages_to_send = [f"Message {i+1}" for i in range(messages_count)]

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # Declare the main queue with dead-lettering and message TTL
    args = {
        "x-dead-letter-exchange": ex_dlx,
        "x-message-ttl": TTL
    }
    channel.queue_declare(queue=queue, durable=True, arguments=args)

    # Declare the dead-letter exchange and the queue bound to it
    channel.exchange_declare(exchange=ex_dlx, exchange_type="direct")
    channel.queue_declare(queue=queue_dlx, durable=True)
    channel.queue_bind(queue=queue_dlx, exchange=ex_dlx)

    for message in messages_to_send:
        if random.random() < probability:
            channel.basic_publish(exchange="", routing_key=queue, body=message)
        else:
            channel.basic_publish(exchange="", routing_key=queue_dlx, body=message)

    # Consume messages from the main queue
    consume_messages(channel, queue)

    connection.close()
