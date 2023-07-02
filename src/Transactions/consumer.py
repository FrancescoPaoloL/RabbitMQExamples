import pika

class Consumer:
    def __init__(self, host, queue_name):
        self.host = host
        self.queue_name = queue_name
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def process_message(self, body):
        # Custom logic to process the received message
        print("Received message: %r" % body)

    def start_consuming(self):
        try:
            while True:
                method_frame, properties, body = self.channel.basic_get(queue=self.queue_name, auto_ack=True)
                if method_frame:
                    self.process_message(body)
                else:
                    break

        except KeyboardInterrupt:
            pass

        finally:
            self.connection.close()

    def _handle_message(self, channel, method, properties, body):
        try:
            self.process_message(body)
            channel.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge message
        except Exception as e:
            print("Failed to process message: %r" % body)
            channel.basic_reject(delivery_tag=method.delivery_tag, requeue=False)  # Reject and discard message

    def close_connection(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()