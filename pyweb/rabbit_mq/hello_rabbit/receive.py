import pika

# connect to RabbitMQ as before
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# make sure the queue exists
channel.queue_declare(queue="hello", durable=True)


# subscribe a callback function to a queue. Whenever we receive a message, this callback will be called by the
# Pika library

def callback(ch, method, properties, body):
    print("[X] Received %r" % body)


# tell RabbitMQ that this particular callback fn should receive messages from our queue

channel.basic_consume(callback, queue="hello", no_ack=True)

# wait for data and run callbacks when necessary
print("[*] Waiting for messages, Press CTRL + C to quit")
channel.start_consuming()
