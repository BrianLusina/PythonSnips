Sample RabbitMQ messaging client as an introduction to using RabbitMQ

1. `send.py` will send a single message to the queue If running on Linux, you will need to install RabbitMQ server using
   these steps
    + `echo 'deb http://www.rabbitmq.com/debian/ stable main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list`
      Adds the APT repository to your etc/apt/sources.list.d
    + `wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -`
      This is optional and is to avoid warnings about unsigned packages, add our public key to your trusted key list
      using apt-key

    + `sudo apt-get update`
      Updates the package list

    + `sudo apt-get install rabbitmq-server`
      install the rabbitmq server package

    That's all. Now you will need to run the server in order for `send.py` to actually send a message
    The command to use is:
    `invoke-rc.d rabbitmq-server stop/start/etc.`
    The server is started as a daemon by default when the RabbitMQ server package is installed.
    Note: The server is set up to run as system user rabbitmq. 
    If you change the location of the Mnesia database or the logs, you must ensure the files are owned by this user (and also update the environment variables).

2. `recieve.py` will recieve the messages from the queue Will start by establishing a connection to RabbitMQ and
   declaring a similar queue. The queue is declared again as one can never know from where the message will be coming
   from. Declaring the queue again will not create another queue, but rather will refer to the same queue in `send.py`.
   To check a list of queues use `sudo rabbitmqctl list_queues`

   A callback needs to be defined, this callback will be called whenever a message is received. It will be called by the
   Pika library
    ``` python
    def callback(ch, method, properties, body):
        print("[*] Recieved message %r: " % r)
    ```

   You will need to tell RabbitMQ that this particular callback fn should receive messages from our queue

   `channel.basic_consume(callback, queue="hello", no_ack=True)`

   After that, start a never ending loop awaiting for a message to come in.
   `channel.start_consuming()`
    


