import time
import random

def consume_messages(channel, queue):
    method_frame, header_frame, body = channel.basic_get(queue=queue, auto_ack=True)
    while method_frame:
        message = body.decode()  # Convert bytes to string
        print("Consumed message:", message)

        # make a delay
        delay = random.uniform(1, 3)
        time.sleep(delay)

        method_frame, header_frame, body = channel.basic_get(queue=queue, auto_ack=True)
