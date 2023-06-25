def read_config(config):
    # Set default properties if they are not present in the config
    messages_count = config.get("messages_count", 1000)
    probability = config.get("probability", 0.5)
    ex_dlx = config.get("ex_dlx", "ex.dlx.messages")
    queue = config.get("queue", "q.messages")
    queue_dlx = config.get("queue_dlx", "q.dlx.messages")
    TTL = config.get("TTL", 20000)

    return messages_count, probability, ex_dlx, queue, queue_dlx, TTL
