This will demonstrate avoiding using resource-intensive tasks expecially for web applications that will have short HTTP request windows. Instead the task is scheduled to be done later.
The task is sent as a message to the queue, which will be popped by a worker process and executed. When many workers are run, the tasks will be shared between them.

