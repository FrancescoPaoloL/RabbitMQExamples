def declare_exchange(channel, exchange_name, exchange_type):
    channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type, durable=True)

def bind_queues_to_exchange(channel, exchange_name, routing_key, queues):
    for queue_name in queues:
        channel.queue_bind(queue=queue_name, exchange=exchange_name, routing_key=routing_key)
