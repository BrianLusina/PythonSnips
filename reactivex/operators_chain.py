"""
We can chain observables to form new observables to subscribe on. This is useful when transforming incoming data and we may want to perform
some pre-processing before we output it to a subscriber/observer.
This chaining of operations creates new observables that we can subscribe to and call the same on_next, on_completed and on_error callbacks

"""
from rx import Observable

greek_words = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
source = Observable.from_(greek_words)

# we map the lengths of each word and get the lengts and create a new observable with a stream of lengths
lengths = source.map(lambda s: len(s))

# now we filter and get the lengths that are greater than or equal to 5
filtered = lengths.filter(lambda i: i >= 5)

# now we can subscribe to the observable and call on_next on our filtered data
filtered.subscribe(lambda value: print("Received {}".format(value)))

print(
    "This will chain the operators on the observable and make this code more readable, eliminating intermidiary variables")

source = Observable.from_(greek_words).map(lambda s: len(s)).filter(lambda i: i >= 5).subscribe(
    lambda value: print("Received {}".format(value)))
