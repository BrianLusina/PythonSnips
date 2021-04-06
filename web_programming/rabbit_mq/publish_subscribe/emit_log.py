import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# create an exchange with name *logs*
channel.exchange_declare(exchange='logs', type="fanout")

message = " ".join(sys.argv[1:] or "Hello RabbitMQ!")

# publish to the named exchange
channel.basic_publish(exchange='logs', routing_key="", body=message)

print("[X] Sent %r" % message)
# close the connection
connection.close()
