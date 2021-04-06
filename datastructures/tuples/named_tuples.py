"""
Simple demo of named tuples
"""
import random
from collections import namedtuple
from string import ascii_letters

A = namedtuple("A", "count enabled color")
tup = A(count=6, enabled=False, color="green")

print(tup.count)  # 6
print(tup.enabled)  # False
print(tup.color)  # green
print(tup)  # A(count=6, enabled=False, color='green')


def generate_tuple():
    """
    generates tuple using namedtuple module. This is much more efficient and ensures that the code
    is maintainable and can be expanded and changed without breaking relying resources on this code
    :return: tuple
    :rtype: tuple
    """
    result = namedtuple("result", "letter number letter_num another_letter")
    letter, number = random.choice(ascii_letters), random.choice(range(len(ascii_letters)))
    letter_num, another_letter = letter + str(number), random.choice(ascii_letters[0: number])

    return result(letter=letter, letter_num=letter_num, number=number, another_letter=another_letter)


if __name__ == "__main__":
    # this enables unpacking the elements
    letter_, letter_num_, number_, another_letter_ = generate_tuple()
    print(letter_, letter_num_, number_, another_letter_, sep="\t")
    # sample output
    # z 33 z33 h
