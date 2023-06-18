def declare_queues(channel, queues):
    for queue_name in queues:
        channel.queue_declare(queue=queue_name, durable=True)
        channel.queue_purge(queue=queue_name)
