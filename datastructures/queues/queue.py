from pprint import pprint

from .fifo import FifoQueue as Queue


class User(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return "{Name: %r, Email: %r, Phone:%r}" % (self.name, self.email, self.phone)


microsoftQueue = Queue()
user = User("Brian Lusina", "awesome@example.com", 123456789)
user1 = User("Bobby Smiles", "bobbysmiles@yahoo.com", 456789)
user2 = User("White Shadow", "whiteshadow@example.com", 123456789)
user3 = User("Grey Hound", "greyhound@example.com", 123456789)

microsoftQueue.enqueue(user)
microsoftQueue.enqueue(user1)
microsoftQueue.enqueue(user2)
microsoftQueue.enqueue(user3)

pprint(microsoftQueue)

# size of queue at beginning
pprint(microsoftQueue.size)

# first person leaves
microsoftQueue.dequeue()

# size of queue after
pprint(microsoftQueue.size)
