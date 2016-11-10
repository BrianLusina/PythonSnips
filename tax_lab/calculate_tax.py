TAX_RATES = {0 / 100: range(0, 1001), 10 / 100: range(1000, 10001), 15 / 100: range(10000, 20201),
             20 / 100: range(20200, 30751),
             25 / 100: range(30750, 50001)}


# , 30: 50000


def calculate_tax(people_sal):
    """
    Calculate the annual tax

    :param people_sal:
    :return:
    """
    result = {}
    # for each key-value pair in TAX_RATES, calculate the rate
    for tax_rate, band in TAX_RATES.items():
        diff = max(band) - min(band)
        for person, salary in people_sal.items():
            if salary > 50000:
                salary *= 0.3
            # check if the salary is greater than max possible in band
            if salary > max(band):
                rate = tax_rate * diff
                results(person, result, rate)
                salary -= diff
                # remaining salary
            elif salary < max(band):
                rate = (salary - min(band)) * tax_rate
                results(person, result, rate)
                break
    return result


def results(person, result, rate):
    """
    Checks if the current person is in the dict, if not adds them with their current rate
    if they are, adds the current rate to the current person
    :param person: the current person
    :param result: the output result
    :param rate: the current tax rate
    :return: the resulting dict
    """
    if person in result:
        result[person] += int(rate)
    else:
        result[person] = int(rate)
    return result


print(calculate_tax({
    "James": 20500,
    "Alex": 500,
    "Kinuthia": 70000
}))
