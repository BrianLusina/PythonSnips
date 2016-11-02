Listening to messages based on a pattern with RabbitMQ

1. `emit_log_topic.py`
    Will emit log messages just like in `Routing` with the only difference being the exchange being used
    
2. `receive_log_topic.py`
    Receives log messages from the queue that have been sent by the producer 