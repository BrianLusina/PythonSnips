class Event:
    def __init__(self):
        self.handlers = set()

    def subscribe(self, func):
        self.handlers.add(func)

    def unsubscribe(self, func):
        self.handlers.remove(func)

    def emit(self, *args):
        for func in self.handlers:
            func(*args)
