import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)


# callback that will handle the task recieved from the queue
def callback(ch, method, properies, body):
    print("[X] Recieved %r" % body)
    time.sleep(body.count(b'.'))
    print("[X] Done.")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue="task_queue")

# wait for data and run callbacks when necessary
print("[*] Waiting for messages, Press CTRL + C to quit")
channel.start_consuming()
