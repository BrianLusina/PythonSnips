import pika

# create a connection to localhost
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

# create an instance of the channel
channel = connection.channel()

# declare the rpc_queue
channel.queue_declare(queue="rpc_queue")


# simple fibonacci sequence, returns the sum of fib numbers up to the provided limit
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    """
    Callback function that is triggered when the server receives a request
    :param ch: Channel to publish the response
    :param method:
    :param props:
    :param body: The limit of the fibonacci series
    :return:
    """
    n = int(body)

    print("Fibonacci result: %r" % fib(n))

    response = fib(n)

    # publish a response
    ch.basic_publish(exchange="", routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print("Awaiting Requests")

channel.start_consuming()
