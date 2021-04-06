def square_evens(my_list):
    return map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, my_list))


print(square_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
