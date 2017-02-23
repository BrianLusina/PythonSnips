def mean(lst):
    nums = [float(i) for i in lst if i.isdigit()]
    strings = "".join([x for x in lst if not x.isdigit()])
    return [sum(nums) / len(nums), strings]
