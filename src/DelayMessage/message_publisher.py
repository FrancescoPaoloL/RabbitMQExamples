import pika

def publish_with_delay(message, delay_ms, expiration_ms, delayed_exchange, delayed_queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=delayed_exchange, exchange_type='x-delayed-message', arguments={
        'x-delayed-type': 'direct'
    })

    channel.queue_declare(queue=delayed_queue, arguments={
        'x-delayed-type': 'direct',
        'x-delayed-message-type': 'direct'
    })

    channel.queue_bind(queue=delayed_queue, exchange=delayed_exchange, routing_key='delayed_queue')

    properties = pika.BasicProperties(
        delivery_mode = 2,  # Make messages persistent
        expiration = str(expiration_ms)  # Set the expiration property to the duration in milliseconds
    )

    channel.basic_publish(
        exchange = delayed_exchange,
        routing_key='delayed_queue',
        body=message,
        properties=properties
    )

    print("Message '{}' published with a delay of {} ms and expiration of {} ms".format(message, delay_ms, expiration_ms))

    connection.close()
