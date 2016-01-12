#!/usr/bin/env python
import pika

# Connetct to broker
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create queue if not already existing
channel.queue_declare(queue='hello')

# Send message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# Gently close connection
connection.close()
