Tests of queueing using Python and RabbitMQ following [this](https://www.rabbitmq.com/getstarted.html) tutorial.

**Hello world**

![Image](img/python-one.png)

**Work queues**

![Image](img/python-two.png)

**Publish/Subscribe**

![Image](img/python-three.png)

**Routing**

![Image](img/python-four.png)

**Topics**

![Image](img/python-five.png)

**Remote Procedure Call (RPC)**

![Image](img/python-six.png)


Commands
--------

List all queues:

    sudo rabbitmqctl list_queues

List all queues including unacknowledged messages

    sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged

List exchanges:

    sudo rabbitmqctl list_exchanges

List bindings:

    sudo rabbitmqctl list_bindings.

Enable management dashboard:

    sudo rabbitmq-plugins enable rabbitmq_management

Access dashboard at http://localhost:15672/

Standard credentials for dashboard: user: guest, pass: guest.
