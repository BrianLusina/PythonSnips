import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_queue(queue="task_queue")


# callback that will handle the task recieved from the queue
def callback(ch, method, properies, body):
    print("[X] Recieved %r" % body)
    time.sleep(body.count(b'.'))
    print("[X] Done.")


channel.basic_consume(callback, queue="task_queue", no_ack=True)

# wait for data and run callbacks when necessary
print("[*] Waiting for messages, Press CTRL + C to quit")
channel.start_consuming()


