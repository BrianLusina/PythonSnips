This will demonstrate avoiding using resource-intensive tasks expecially for web applications that will have short HTTP
request windows. Instead the task is scheduled to be done later. The task is sent as a message to the queue, which will
be popped by a worker process and executed. When many workers are run, the tasks will be shared between them.

1. `new_tasks.py`
   Will send strings that stand for complex tasks. Using the time.sleep() function we will assume a busy task. We'll
   take the number of dots in the string as its complexity; every dot will account for one second of "work". For
   example, a fake task described by Hello... will take three seconds. Will modify the `send.py` from `HelloRabbit`
   package to allow arbitrary messages to be sent from the command line

2. `worker.py`
   Will take a second of work for every dot in the message body it will recieve from `new_task.py`. It will pop messages
   from the queue and perform the task Multiple workers can be opened and tasks will be divided up among the open
   workers

To run the program, run the `worker.py` in seperate consoles and publish messages from `new_tasks.py` from another
console

Console 1

``` bash
python new_task First message.
python new_task second message..
python new_task third message...
python new_task fourth message....
python new_task fifth message.....
```

Console 2

``` bash
python worker.py
[*] Waiting for messages, Press CTRL + C to quit
[X] Received 'First message.'
[x] Received 'Third message...'
[x] Received 'Fifth message.....'
```

Console 3

``` bash
python worker.py
[*] Waiting for messages, Press CTRL + C to quit
[x] Received 'Second message..'
[x] Received 'Fourth message....'
```

Read more [here](https://www.rabbitmq.com/tutorials/tutorial-two-python.html) on message acknowkledgement, durability
and fair dispatch
