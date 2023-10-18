from bisect import bisect_left
from typing import List


def successful_pairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    pairs = []

    sorted_potions = sorted(potions)

    for spell in spells:
        middle = (success + spell - 1) // spell
        count = len(sorted_potions) - bisect_left(sorted_potions, middle)
        pairs.append(count)

    return pairs


def successful_pairs_2(spells: List[int], potions: List[int], success: int) -> List[int]:
    def valid_position(sorted_potions: List[int], target: int, current_spell: int) -> int:
        """This retrieves the first position of a potion which if multiplied with a spell returns at least the given
        strength

        Args:
            sorted_potions (List): list of sorted potions
            target (int): success.
            current_spell (int): spell.

        Returns:
            index of the first potion that will return at least success when multiplied with spell
        """
        potion_needed = (target + current_spell - 1) // current_spell
        left, right = 0, len(sorted_potions)

        while left < right:
            middle = (left + right) >> 1

            if sorted_potions[middle] >= potion_needed:
                right = middle
            else:
                left = middle + 1
        return left

    pairs = []
    potions.sort()

    for spell in spells:
        count = len(potions) - valid_position(potions, success, spell)
        pairs.append(count)

    return pairs
