"""
In this case, we simply use Observable.from_([iterable]) which will take an observable and call on_next on each item and call on_completed
when it reaches the end, This allows use to pass an iterable object to an obserble and subscribe an observer to it
"""
from rx import Observable, Observer


class PrintObserver(Observer):
    """
    Custom observer
    """

    def on_next(self, value):
        print("Received {}".format(value))

    def on_error(self, error):
        print("Error encountered {}".format(error))

    def on_completed(self):
        print("Done")


greek_words = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
source = Observable.from_(greek_words)

source.subscribe(PrintObserver())
