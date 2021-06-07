"""
n top of data, Observables can also emit pubsub. By treating data and pubsub the same way, you can do powerful compositions to make the two work together. Below, we have an Observable that emits a consecutive integer every 1000 milliseconds. This Observable will run infinitely and never call on_complete.
"""
from rx import Observable

Observable.interval(1000).map(lambda i: "{} Mississipi".format(i)).subscribe(lambda s: print(s))

# this will stop the sequence
input("Press any key to exit\n")
