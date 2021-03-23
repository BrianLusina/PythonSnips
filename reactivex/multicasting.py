"""
Each Subscriber to an Observable often will receive a separate stream of emissions. For instance, having two subscribers to this Observable emitting three random integers will result in both subscribers getting different numbers.
"""
from rx import Observable

from random import randint


three_emissions = Observable.range(1, 3)

three_random_ints = three_emissions.map(lambda i: randint(1, 100000))

three_random_ints.subscribe(lambda i: print("Subscriber 1 Received: {0}".format(i)))
three_random_ints.subscribe(lambda i: print("Subscriber 2 Received: {0}".format(i)))

