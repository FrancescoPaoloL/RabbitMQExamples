from config_reader import read_config
from producer import Producer
from consumer import Consumer

def main():
    host, probability, queue = read_config("config.yaml")

    producer = Producer(host, queue)
    consumer = Consumer(host, queue)

    # Connect to RabbitMQ
    producer.connect()
    consumer.connect()

    # Produce 100 messages
    for i in range(1, 101):
        message = f"Message {i}"
        producer.publish_message(message, probability)

    # Start consuming messages
    consumer.start_consuming()

    # Close connections
    producer.close_connection()
    consumer.close_connection()

if __name__ == "__main__":
    main()
