TAX_RATES = {0 / 100: range(0, 1001),
             10 / 100: range(1000, 10001),
             15 / 100: range(10000, 20201),
             20 / 100: range(20200, 30751),
             25 / 100: range(30750, 50001)
             }


def calculate_tax(people_sal):
    """
    Calculate the annual tax
    Get the salary of each person and check if it falls within a certain tax band, if it does, calculate backwards
    to get the tax for each band while reducing the salary.

    :param people_sal: a dictionary containing people's salary with names as keys and salary as values
    :return: taxes for people a s a dictionary
    :rtype:dict
    """

    # end result
    result = {}

    # store to keep record of already calculated tax band
    memo = {}

    # for each key-value pair in TAX_RATES, calculate the rate
    for tax_rate, band in TAX_RATES.items():

        # check if the person's salary falls within a certain band
        for person, salary in people_sal.items():

            tax = 0
            print("Current memo>", memo)

            # add band to the memo store to keep record of an already calculated band
            # if the tax band is not in the store, start the calculation
            if tax_rate not in memo:

                # if the salary is greater than current maximum tax band, calculate the tax for this band
                # then reduce the salary by the max band
                if salary > max(band):
                    print("Salary in band ", salary, " band ", band)

                    # salary diff for the current band
                    # get the difference between the maximum possible tax rate and the lowest possible
                    diff = max(band) - min(band)

                    print("Tax difference: ", diff, " tax rate: ", tax_rate)

                    # calculate the tax
                    tax += tax_rate * diff
                    print("Tax, ", tax)

                    # reduce the salary by the diff
                    salary -= diff
                    print("new current salary: ", salary)

                    # check if the person's tax data is in the result, add it if not
                    update_results(person, result, tax)

                    # add this band to the store
                    memo[tax_rate] = band

                # the current salary is not greater than the maximum band
                # but it is in the band range
                elif salary in band:
                    print("Salary ", salary, " in last band:", band)

                    # the salary minus the lowest possible amount in the band
                    diff = salary - min(band)

                    # calculate the tax
                    tax += tax_rate * diff
                    # reduce the salary by the diff
                    salary -= diff
                    print("new current salary in last band: ", salary)

                    update_results(person, result, tax)

                    # add this band to the store
                    memo[tax_rate] = band
                # the tax band is in the memo, but the salary is still greater than 0
                elif salary > 0:
                    print("Salary still greater than 0 and", salary, " memo full", memo)
    return result


def update_results(person, result, tax):
    """
    Checks if the current person is in the dict, if not adds them with their current rate
    if they are, adds the current rate to the current person
    :param tax:
    :param person: the current person
    :param result: the output result
    :return: the resulting dict
    """
    if person in result:
        result[person] += tax
    else:
        result[person] = tax


print(calculate_tax({
    # "James": 20500,
    # "Alex": 500,
    "Kinuthia": 70000
}))

# output
# {
#     ‘Alex’: 0,
#     ‘James’: 2490,
#     ‘Kinuthia’: 15352.5
# }
