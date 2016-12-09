def find_longest(string):
    spl = string.split()
    number_list = []
    for i in spl:
        number_list.append(len(i))
    return max(number_list)
