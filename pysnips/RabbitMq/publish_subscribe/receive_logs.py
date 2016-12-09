import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# create an exchange with name *logs*
channel.exchange_declare(exchange='logs', type="fanout")

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# bind our exchange to the randomly name queue
channel.queue_bind(exchange='logs', queue=queue_name)

# print statement to display waiting method

print("[X] Waiting for logs. To exit press CTRL + C")


def callback(ch, method, properties, body):
    print("[X] Received log: %r" % body)


channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
