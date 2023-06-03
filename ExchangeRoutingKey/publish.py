import pika

def publish_messages(channel, exchange_name, nr_messages):
    delivery_tags = []
    for i in range(nr_messages):
        result = channel.basic_publish(exchange=exchange_name, routing_key=str(i), body=f"Message #{i}", properties=pika.BasicProperties())
        if result:
            delivery_tags.append(result)
    return delivery_tags

def wait_for_confirmation(channel, delivery_tags):
    for tag in delivery_tags:
        channel.wait_for_confirmation(tag)
