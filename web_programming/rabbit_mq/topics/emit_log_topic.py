import sys

import pika

# set up a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# create a channel
channel = connection.channel()

# declare the exchange which will be a topic type
channel.exchange_declare(exchange="topic_logs", type='topic')

# get the routing key from the terminal else set a default
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

# set a message from terminal or set a default if none is provided
message = " ".join(sys.argv[2:]) or "Hello RabbitMQ"

# publish the message
channel.basic_publish(exchange="topic_logs", routing_key=routing_key, body=message)

print("[X] Message Sent (%r,%r)" % (routing_key, message))

# close the connection
connection.close()
