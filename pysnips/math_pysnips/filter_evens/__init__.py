def filter_me(num_list):
    evens = filter(lambda x: x % 2 == 0, num_list)
    return list(evens)
