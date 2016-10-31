This will demonstrate avoiding using resource-intensive tasks expecially for web applications that will have short HTTP request windows. Instead the task is scheduled to be done later.
The task is sent as a message to the queue, which will be popped by a worker process and executed. When many workers are run, the tasks will be shared between them.

1. `new_tasks`
    Will send strings that stand for complex tasks. Using the time.sleep() function we will assume a busy task. We'll take the number of dots in the string as its complexity; every dot will account for one second of "work". For example, a fake task described by Hello... will take three seconds.
    Will modify the `send.py` from `HelloRabbit` package to allow arbitrary messages to be sent from the command line