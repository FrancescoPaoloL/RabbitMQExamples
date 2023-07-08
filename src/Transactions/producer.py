import pika
import random

class Producer:
    def __init__(self, host, queue_name):
        self.host = host
        self.queue_name = queue_name
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def publish_message(self, message, probability):
        try:
            self.channel.tx_select()  # Start transaction
            self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=message)
            
            # Simulate randomly occurring error
            if random.random() < probability:
                raise Exception("Random error occurred")
            
            self.channel.tx_commit()  # Commit transaction
            print("Message sent: %r" % message)
        except:
            self.channel.tx_rollback()  # Rollback transaction
            print("Failed to send message: %r" % message)

    def close_connection(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
