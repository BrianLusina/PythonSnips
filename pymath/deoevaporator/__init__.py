from math import ceil, log


def evaporator(content, evap_per_day, threshold):
    nth_day = 0
    limit = content * (threshold / 100)

    while content >= limit:
        content -= content * (evap_per_day / 100)
        nth_day += 1

    return nth_day


def evaporator_2(content, evap_per_day, threshold):
    return ceil(log(threshold / 100.0) / log(1.0 - evap_per_day / 100.0))
