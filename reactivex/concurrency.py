import multiprocessing
import random
import time
from threading import current_thread

from rx import Observable
from rx.concurrency import ThreadPoolScheduler


def intense_calc(value):
    """This simply emulates a long running calculation/operation"""
    time.sleep(random.randint(5, 20) * .1)
    return value


# calculate the number of CPUs and then determine the number of threads to use
thread_count = multiprocessing.cpu_count()
pool_scheduler = ThreadPoolScheduler(thread_count)

greek_words = ["Alpha", "Epsilon", "Beta", "Gamma", "Delta"]
# create processes

# process 1
Observable.from_(greek_words).map(lambda s: intense_calc(s)).subscribe_on(pool_scheduler).subscribe(
    on_next=lambda s: print("PROCESS 1: {0} {1}".format(current_thread().name, s)),
    on_error=lambda e: print(e),
    on_completed=lambda: print("PROCESS 1 done!"))

# process 2
Observable.range(1, 10).map(lambda s: intense_calc(s)).subscribe_on(pool_scheduler).subscribe(
    on_next=lambda i: print("PROCESS 2: {0} {1}".format(current_thread().name, i)),
    on_error=lambda e: print(e), on_completed=lambda: print("PROCESS 2 done!"))

# Create Process 3, which is infinite
Observable.interval(1000) \
    .map(lambda i: i * 100) \
    .observe_on(pool_scheduler) \
    .map(lambda s: intense_calc(s)) \
    .subscribe(on_next=lambda i: print("PROCESS 3: {0} {1}".format(current_thread().name, i)),
               on_error=lambda e: print(e))
