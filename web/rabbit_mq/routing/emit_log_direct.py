import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# declare the exchange to use
channel.exchange_declare(exchange="direct_logs", type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = " ".join(sys.argv[2:] or "Hello RabbitMQ!")

# publish the message
channel.basic_publish(exchange="direct_logs", routing_key=severity, body="message")

print("[X] Sent: %r:%r" % (severity, message))
connection.close()
