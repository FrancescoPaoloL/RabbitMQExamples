import pika
from consume import consume_messages 

def rescue_lost_messages(config):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    queue = config.get('queue', 'q.messages')
    queue_dlx = config.get('queue_dlx', 'q.dlx.messages')

    # Consume messages from q.dlx.messages and re-publish them to q.messages
    method_frame, header_frame, body = channel.basic_get(queue=queue_dlx, auto_ack=True)
    while method_frame:
        channel.basic_publish(exchange='', routing_key=queue, body=body)
        method_frame, header_frame, body = channel.basic_get(queue=queue_dlx, auto_ack=True)

    print(f"Rescue operation completed. Lost messages have been sent back to {queue}")
    consume_messages(channel, queue)
    connection.close()
