# RabbitMQ examples
RabbitMQ is a message broker that enables communication between different components of an application. It implements the Advanced Message Queuing Protocol (AMQP) and provides a flexible messaging system for building distributed systems.
This repository contains basic concepts related to RabbitMQ.


- ## Get Info
    This code retrieves the RabbitMQ overview, list of queues, and list of exchanges, and prints them in a tabular format using the tabulate library.

- ## ExchangeRoutingKey
    An exchange in RabbitMQ plays a vital role in directing messages to queues based on their routing keys. It serves as a distribution mechanism, determining how messages are allocated among the queues. RabbitMQ offers an extension that employs a consistent hashing algorithm for message routing; you can install it with: 

    ```
    rabbitmq-plugins enable rabbitmq_consistent_hash_exchange
    ```
    This algorithm guarantees that messages with identical routing keys consistently reach the same queue, even if the number of queues or consumers changes over time. By utilizing the x-consistent-hash exchange type, you can ensure that messages sharing the same routing key will always be directed to the same queue. The code publishes a large number of messages to the exchange, confirms the successful delivery of each message, waits for a specified period of time, and then evaluates the results.

- ## DLX
    DLX stands for Dead-Letter Exchange and is used when a message fails to be delivered or gets rejected by a queue, it can be redirected to this kind of exchange.
    Once the message reaches it, you can decide what to do with it: you can either discard it or
    send it to another queue for further processing.

    Messages can be mainly rejected because:
    - Messages is negatively (ack)nowledged
    - TTL expired (aka Time To Live, it represents a time limit on how long a message can stay in a queue before it expires.)
    - Message is dropped for queue exceeded lenght limit.
    
    In this example, we are simulating the consumption of messages with a time-to-live (TTL) of 20 seconds. We generate 10 messages and randomly assign each message an accept or reject state. The messages are consumed with a delay. After the consumption process, we prompt the user to decide whether they want to rescue the messages in the dead-letter exchange (DLX). If the user chooses to rescue the messages, we move them back to the original queue, where they will be consumed again using the same process as before.

- ## DelayMessage
    This script sends two messages to the RabbitMQ broker. One message is delayed by a specified delay in milliseconds, while the other message is delayed until the next specified day and hour. 
    
    To accomplish this, you need to install the rabbitmq_delayed_message_exchange" plugin by following these steps:
    
    ```
    1. Download the latest ".ez" file from the following URL: https://github.com/rabbitmq/rabbitmq-delayed-message-exchange/releases. At the time of writing, I placed the latest file in the "other" folder.
    
    2. Open a terminal or command prompt and enter the following command: "rabbitmq-plugins enable rabbitmq_delayed_message_exchange --online".
    ```
    
- ## Transactions
    Transactions in RabbitMQ allow you to group multiple operations into a single atomic unit. This ensures that either all operations within the transaction are successfully processed, or none of them are. Transactions provide message integrity and consistency, especially in the event of failures or errors. In this example, we simulate random errors to demonstrate how transactions work and showcase their benefits.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Languages and Tools
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Requirements
```
pika==1.3.1
PyYAML==6.0
```

## Test Coverage
### On DelayMessage

| Name                  | Stmts | Miss | Branch | BrPart | Cover |
|-----------------------|-------|------|--------|--------|-------|
| config_reader.py      | 13    | 0    | 0      | 0      | 100%  |
| config_reader_test.py | 31    | 1    | 4      | 1      | 94%   |
| datetime_calculator.py| 8     | 8    | 0      | 0      | 0%    |
| message_publisher.py  | 24    | 24   | 0      | 0      | 0%    |
| <b>TOTAL</b>     | <b>76</b>  | <b>33</b>| <b>4</b>|<b>1</b>|<b>41%</b>|

todo...


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>



