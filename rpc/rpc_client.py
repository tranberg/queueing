#!/usr/bin/env python
import pika
import uuid
import random
import time


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        # Declare an exclusive callback queue to receive answer
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to=self.callback_queue,
                                                                   correlation_id=self.corr_id),
                                   body=str(n))
        # Block until answer is received or timeout
        start = time.time()
        while self.response is None:
            self.connection.process_data_events()
            if time.time() - start > 2:
                self.response = "Error, server not responding"
        return str(self.response)

fibonacci_rpc = FibonacciRpcClient()
t = time.time()
for i in range(10):
    n = int(random.random() * 20)
    print(" [x] Requesting fib(%r)" % n)
    response = fibonacci_rpc.call(n)
    print(" [.] Got %r" % response)
    if 'Error' in response:
        break
