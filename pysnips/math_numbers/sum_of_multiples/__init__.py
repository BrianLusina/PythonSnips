def sum_of_multiples(limit, multiples):
    if multiples[0] == 0:
        multiples = multiples[1:]
    return sum(value for value in range(limit)
               if any(value % multiple == 0
                      for multiple in multiples))