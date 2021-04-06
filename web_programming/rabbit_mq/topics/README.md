Listening to messages based on a pattern with RabbitMQ

1. `emit_log_topic.py`
   Will emit log messages just like in `Routing` with the only difference being the exchange being used

2. `receive_log_topic.py`
   Receives log messages from the queue that have been sent by the producer

To receive all the logs run:

```bash
python receive_logs_topic.py "#"
```

To receive all logs from the facility "kern":

```bash
python receive_logs_topic.py "kern.*"
```

Or if you want to hear only about "critical" logs:

```bash
python receive_logs_topic.py "*.critical"
```

You can create multiple bindings:

```bash
python receive_logs_topic.py "kern.*" "*.critical"
```

And to emit a log with a routing key "kern.critical" type:

```bash
python emit_log_topic.py "kern.critical" "A critical kernel error"
```
