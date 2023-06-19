# RabbitMQ examples
RabbitMQ is a message broker that enables communication between different components of an application. It implements the Advanced Message Queuing Protocol (AMQP) and provides a flexible messaging system for building distributed systems.
This repository contains basic concepts related to RabbitMQ.

- ## ExchangeRoutingKey
    An exchange in RabbitMQ plays a vital role in directing messages to queues based on their routing keys. It serves as a distribution mechanism, determining how messages are allocated among the queues. RabbitMQ offers an extension that employs a consistent hashing algorithm for message routing; you can install it with: 

    ```
    rabbitmq-plugins enable rabbitmq_consistent_hash_exchange
    ```
    This algorithm guarantees that messages with identical routing keys consistently reach the same queue, even if the number of queues or consumers changes over time. By utilizing the x-consistent-hash exchange type, you can ensure that messages sharing the same routing key will always be directed to the same queue. The code publishes a large number of messages to the exchange, confirms the successful delivery of each message, waits for a specified period of time, and then evaluates the results.

- #### TODO...

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Languages and Tools
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Requirements
```
pika==1.3.1
PyYAML==6.0
```

## Test coverage
TODO

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>



