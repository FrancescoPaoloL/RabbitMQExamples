from producer import Producer
from consumer import Consumer

producer = Producer('localhost', 'my_queue')
producer.connect()

consumer = Consumer('localhost', 'my_queue')
consumer.connect()

# Produce 100 messages
for i in range(1, 101):
    message = f"Message {i}"
    producer.publish_message(message)

# Start consuming messages
consumer.start_consuming()

producer.close_connection()
consumer.close_connection()