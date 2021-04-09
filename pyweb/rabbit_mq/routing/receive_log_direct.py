import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# declare the exchange to match the one from the producer
channel.exchange_declare(exchange='direct_logs', type='direct')

# declare a queue, and give it a random name
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]

if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

print("[*] Waiting for logs, press CTRL + C to quit")


# callback method to be handled by the channel
def callback(ch, method, properties, body):
    print("[X] Received: %r:%r" % (method.routing_key, body))


channel.basic_consume(callback, queue=queue_name, no_ack=True)

# start listening for messages
channel.start_consuming()
