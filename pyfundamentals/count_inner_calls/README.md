The aim of this kata is to determine the number of sub-function calls made by an unknown function.

You have to write a function named count_calls which:

takes as parameter a function and its arguments (args, kwargs)

calls the function

returns a tuple containing:

the number of function calls made inside it and inside all the sub-called functions recursively

the function return value.

NB: The call to the function itself is not counted.

HINT: The sys module may come in handy.