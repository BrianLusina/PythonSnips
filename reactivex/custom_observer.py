"""
This is a simple demonstration of a custom Observable implementing on_next, on_error and on_completed callbacks
This is used when one wants to have their own callbacks executed when a stream comes in
"""
from rx import Observable, Observer


def push_strings(observer):
    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()


class PrintObserver(Observer):
    def on_next(self, value):
        print("Received {}".format(value))

    def on_error(self, error):
        print("Error encountered {}".format(error))

    def on_completed(self):
        print("Done")


source = Observable.create(push_strings)

source.subscribe(PrintObserver())
