def decode(string):
    d = {1: 9, 2: 8, 3: 7, 4: 6, 5: 0, 9: 1, 8: 2, 7: 3, 6: 4, 0: 5}
    m = [str(d.get(int(i))) for i in string]
    return "".join(m)
