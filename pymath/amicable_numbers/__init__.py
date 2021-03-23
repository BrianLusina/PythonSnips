def sum_amicable_numbers(limit):
    """
    Sums all amicable numbers under the given limit
    :param limit: Upper Limit to find sum of all amicable numbers
    :return: sum of all amicable numbers under given limit
    :rtype: int
    """
    amicable_numbers = set()
    for number in range(limit):
        if number not in amicable_numbers:
            sum_1 = sum_of_divisors_of_number(number)

            sum_2 = sum_of_divisors_of_number(sum_1)

            if number == sum_2 and number != sum_1:
                amicable_numbers.add(number)

    return sum(amicable_numbers)


def sum_of_divisors_of_number(number):
    return sum([x for x in range(1, number) if number % x == 0])
