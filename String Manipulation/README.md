# String Manipulation

Series of problems and solutions to String manipulation in Python. Of course there are dozens of other ways to solve these problems.
Here is a breakdown of challenges and their descriptions

## Denumerate String
You have to rebuild a string from an enumerated list.

the function only accepts a list of tuples where each tuple consists of 2 elements
the first element of the tuple will be the index of the reconstructed string and the second element a single alphanumeric character
the indexes must start from zero and must match with how indexes are numbered normally, so gaps between indexes are not allowed
tuples don't have to be ordered by the indexes
The function should return False otherwise.

Input example:

[(4,'y'),(1,'o'),(3,'t'),(0,'m'),(2,'n')]
Returns
'monty'

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