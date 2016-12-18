def median(lst):
    """
    func to find median in a list
    """
    sort_list = sorted(lst)
    med = 0
    if len(sort_list) == 1:
        med = sort_list[0]
    elif len(sort_list) % 2 == 0:
        f_mid_index = len(sort_list) / 2
        s_mid_index = f_mid_index - 1
        med = (sort_list[f_mid_index] + sort_list[s_mid_index]) / 2.0
    elif len(sort_list) % 2 != 0:
        f_mid_index = (len(sort_list) / 2)
        med = sort_list[f_mid_index]
    return med
