#!/usr/bin/env python
from connect import Get

get = Get()

connection = get.connection
channel = get.channel

# Creates a message queue
channel.queue_declare(queue='hello')

# Send the message
for i in range(1000):
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Fuck off wanker...')
    print(" [x] Sent 'Hello World!'")

# Close connection to ensure message sends
connection.close()