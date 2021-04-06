import sys

import pika

message = " ".join(sys.argv[1:] or "Hello RabbitMQ!")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)

channel.basic_publish(exchange="",
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2)  # make message persistent
                      )
print("[X] Sent %r" % message)

# close the connection
connection.close()
