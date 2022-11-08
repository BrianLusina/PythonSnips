from typing import List
from fractions import Fraction


def gearing_up_for_destruction(pegs: List[int]) -> List[int]:
    if not pegs:
        return [-1, -1]

    number_of_pegs = len(pegs)
    is_even = number_of_pegs % 2 == 0
    general_sum = 0

    for idx, peg in enumerate(pegs[1:-1]):
        sign = 1 if idx % 2 == 0 else -1
        general_sum += sign * peg

    if is_even:
        all_sum = 2 * float(-pegs[0] + 2 * general_sum + pegs[-1]) / 3
    else:
        all_sum = 2 * (-pegs[0] + 2 * general_sum - pegs[-1])

    first_gear_radius = Fraction(all_sum).limit_denominator()

    if first_gear_radius < 2:
        return [-1, -1]

    current_radius = first_gear_radius
    for idx in range(number_of_pegs - 1):
        center_distance = pegs[idx + 1] - pegs[idx]
        next_radius = center_distance - current_radius

        if current_radius < 1 or next_radius < 1:
            return [-1, -1]
        else:
            current_radius = next_radius

    return [first_gear_radius.numerator, first_gear_radius.denominator]
