#!/usr/bin/env python
import pika

# Connetct to broker
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create queue if not already existing
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Get messages from queue and deliver to callback function
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
# Never-ending loop polling the queue for messages
channel.start_consuming()
