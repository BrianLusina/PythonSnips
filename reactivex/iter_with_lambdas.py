"""
Here we use an Observable.from_ and lambdas in the subscribe of the observer, this means we do not have to implement our own observer
and we can simply use lambdas to call the on_next, on_error and on_completed callbacks on the subscriber
"""
from rx import Observable

greek_words = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
source = Observable.from_(greek_words)

source.subscribe(
    on_next=lambda value: print("Received {}".format(value)),
    on_error=lambda error: print("Error encounted {}".format(error)),
    on_completed=lambda: print("Done")
)
print(
    "We can even eliminate the on_<> callbacks in the subscriber and simply use the on_next callback, not recommended in production")

source.subscribe(lambda value: print("Recieved {}".format(value)))
