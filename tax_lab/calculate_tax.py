TAX_RATES = {0: range(0, 1001), 10: range(1000, 10001), 15: range(10000, 20201), 20: range(20200, 30751),
             25: range(30750, 50001)}
#, 30: 50000


def calculate_tax(people_sal):
    """
    Calculate the annual tax

    :param people_sal:
    :return:
    """
    # total variable for tax
    result = {}
    # for each key-value pair in TAX_RATES, calculate the rate
    for tax in TAX_RATES:
        for person in people_sal:
            # check if salary is greater than current max
            if people_sal[person] > max(TAX_RATES[tax]):
                diff = max(TAX_RATES[tax]) - min(TAX_RATES[tax])
                rate = (tax / 100) * diff

                # check if key is in dict
                if person in result:
                    result[person] += rate
                else:
                    result[person] = rate

                # subtract the diff from salary
                people_sal[person] -= diff

                # check if person salary is still valid
                if people_sal[person] == 0:
                    break
    return result

print(calculate_tax({
    "Alex": 0,
    "James": 2490,
    "Kinuthia": 15352.5
}))


