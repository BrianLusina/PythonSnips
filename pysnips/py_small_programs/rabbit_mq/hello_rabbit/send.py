import pika

"""
Making a connection to a broker on the local machine - hence the localhost.
If we wanted to connect to a broker on a different machine we'd simply specify its name or IP address here.
"""
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# create a queue to which the message will be delivered

channel.queue_declare(queue="hello", durable=True)

# creating a default exchange identified by an empty string
# it allows us to specify to exactly which queue the message will go
# This queue name needs to be identified by the *routing* key parameter
channel.basic_publish(exchange="",
                      routing_key='hello',
                      body="Hello world!")
print("[x] Sent 'Hello World' ")

# closing the connection
connection.close()
