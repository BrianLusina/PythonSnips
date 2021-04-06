Small program the delivers the same message to different workers using RabbitMQ

1. `emit_log.py`
   Emits Logs to an Exchange which will handle the transmission to the availabled queues

   This is used to list all the available exchanges `sudo rabbitmqctl list_exchanges`
   Used to list all available bindings `sudo rabbitmqctl list_bindings`

2. `receive_logs.py`
   Receives the logs and displayes them on the screen.