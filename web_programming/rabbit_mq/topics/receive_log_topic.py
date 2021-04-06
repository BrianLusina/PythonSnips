import sys

import pika

# open a connection to localhost
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

# declare a channel
channel = connection.channel()

# declare the exchange to use which will match the producer
channel.exchange_declare(exchange='topic_logs', type='topic')

# exclusively declare a channel which will give a random name, save the random name in a variable
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# retrieve the binding keys
binding_keys = sys.argv[1:]

# implicit truthy
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

# for each key bind it to a queue and the exchange
for binding_key in binding_keys:
    channel.queue_bind(exchange="topic_logs", queue=queue_name, routing_key=binding_key)

print("[*] Waiting for for logs. To exit press CTRL+C")


# create callback to handle messages received
def callback(ch, method, properties, body):
    print("[X] Message <RoutingKey:%r, Body: %r>" % (method.routing_key, body))


channel.basic_consume(callback, queue=queue_name, no_ack=True)

# await the messages from queue
channel.start_consuming()
