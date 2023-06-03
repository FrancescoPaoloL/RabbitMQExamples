import pika

def establish_connection(host):
    return pika.BlockingConnection(pika.ConnectionParameters(host=host))
