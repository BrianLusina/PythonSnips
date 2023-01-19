# Dynamic Array

Declare a 2-dimensional array, arr, of n empty arrays. All arrays are zero indexed.
Declare an integer, lastAnswer, and initialize it to 0.

There are 2 types of queries, given as an array of strings for you to parse:

1. Query: 1 x y
    - Let idx = (x^lastAnswer %) n.
    - Append the integer y to arr[idx].
2. Query: 2 x y
    - Let idx = (x ^lastAnswer) % n.
    - Assign the value arr[idx][y% size(arr[idx])] to lastAnswer.
    - Store the new value of lastAnswer to an answers array.

Note: ^ is the bitwise XOR operation, % is the modulo operator.
Finally, size(arr[idx]) is the number of elements in arr[idx]

Complete the dynamicArray function below.

dynamicArray has the following parameters:

- int n: the number of empty arrays to initialize in arr
- queries[q]: query strings that contain 3 space-separated integers

Returns:

- int[]: the results of each type 2 query in the order they are presented
