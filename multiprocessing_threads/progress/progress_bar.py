from threading import Thread


class ProgressBar(Thread):
    """
        class for running progress process
        against a list of function calls
    """

    def __init__(self, queue):
        """
        Create a ProgressBare worker instance
        """
        Thread.__init__(self)
        self.queue = queue
        # get the size of the queue, which is the number of functions to execute
        self.total_count = self.queue.qsize()
        self.processed_count = 0

    def run(self):
        """
        We want to run the function until all tasks in the queue are complete.
        The self.queue.get() is a blocking function and once the function is executed. The Main thread
        is made aware of the completion of a task. Calling self.queue.task_done() indicates a task is done
        we can increment the processed_count
        """
        while True:
            func = self.queue.get()
            func()
            self.queue.task_done()
            self.processed_count += 1

    def percent_done(self):
        """
        Report on the percentage done for the thread
        """
        return float(self.processed_count) / float(self.total_count)

# queue = Queue()
# funcs = [add_to_cpanel(self.employee), add_to_seafile(self.employee), 
#         send_email('webmaster@tezzasolutions.com',
#             'harrison.kamau@tezzasolutions.com',
#             'harrison.kamau@tezzasolutions.com',
#             'New User Info',
#             'mailer/user_info',
#             data=EmployeeEmailData()
#         ]
# # you can specify more workers based on your own factors
# for x in range(10):
#     worker = ProgressBar(queue)
#     # Setting daemon to True will let the main thread exit even though the workers are blocking
#     worker.daemon = True
#     worker.start()

# for func in funcs:
#     queue.put(func)
# # Causes the main thread to wait for the queue to finish processing all the tasks
# queue.join()
