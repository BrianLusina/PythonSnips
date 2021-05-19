from typing import Tuple, List


def max_duffel_bag_value(cake_tuples: List[Tuple[int, int]], capacity: int):
    """
    Calculates the value of a duffel bag give a list of tuples of cakes which contain weight
    of each cakes and their value(monetary) and the capacity the bag can carry
    :param cake_tuples: list of tuples of cakes
    :param capacity: max capacity the duffel bag can carry
    :return: maximum value of the duffel bag
    """

    # list to hold maximum possible value at every duffel bag weight capacity from 0 to
    # weight capacity starting each index with value of 0
    max_values_at_capacity = [0] * (capacity + 1)

    for current_capacity in range(capacity + 1):

        # set a variable to hold the max monetary value so far for current_capacity
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples:

            # if a cake weighs 0 and has a positive value the value of our duffel bag is
            #  infinite!
            if cake_weight == 0 and cake_value != 0:
                return float('inf')

            # if the current cake weighs as much or less than the current weight capacity
            # it's possible taking the cake would get a better value
            if cake_weight <= current_capacity:
                # so we check: should we use the cake or not?
                # if we use the cake, the most kilograms we can include in addition to the
                #  cake
                # we're adding is the current capacity minus the cake's weight. we find the
                #  max
                # value at that integer capacity in our list max_values_at_capacities
                max_value_using_cake = cake_value + max_values_at_capacity[current_capacity - cake_weight]

                # now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake, current_max_value)

        # add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_values_at_capacity[current_capacity] = current_max_value

    return max_values_at_capacity[capacity]
