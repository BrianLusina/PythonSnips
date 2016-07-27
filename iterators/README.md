# Iterators

These are a series of iterator function problems. Some may include lists, tuples, dictionaries, sets and the likes. However, the main focus here will be on the use of generotor functions, such as **yield**

Here is a breakdown of all the problems and their description.s

## Multi-range iterator

This is a beta description, please, help me to fix it.

Let's look at the following generator:

```python
def gen():
    for i in range(2):
        for j in range(3):
            yield (i, j)
If we print all yielded values, we'll get

(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
```

For a given parameter list N you must return an iterator, which goes through all possible tuples A, where Ai changes from 0 to Ni.

## Count vegetables

Help Suzuki count his vegetables....

Suzuki is the master monk of his monastery so it is up to him to ensure the kitchen is operating at full capacity to feed his students and the villagers that come for lunch on a daily basis.

This week there was a problem with his deliveries and all the vegetables became mixed up. There are two important aspects of cooking in his kitchen, it must be done in harmony and nothing can be wasted. Since the monks are a record keeping people the first order of business is to sort the mixed up vegetables and then count them to ensure there is enough to feed all the students and villagers.

You will be given a string with the following vegetables:

"cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"
Return a list of tuples with the count of each vegetable in descending order. If there are any non vegetables mixed in discard them. If the count of two vegetables is the same sort in descending alphabetical order.
``` python
(119, "pepper"),
(114, "carrot"),
(113, "turnip"),
(102, "onion"),
(101, "tofu"),
(100, "cabbage"),
(93, "mushroom"),
(90, "cucumber"),
(88, "potato"),
(80, "celery")
```