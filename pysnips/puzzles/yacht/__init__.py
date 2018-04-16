from collections import Counter
from functools import partial

# Score categories
# Change the values as you see fit
YACHT , ONES , TWOS , THREES , FOURS , FIVES , SIXES , FULL_HOUSE , FOUR_OF_A_KIND , LITTLE_STRAIGHT , BIG_STRAIGHT, CHOICE = range(0, 12)


def yacht(dice):
    return 50 if len(set(dice)) == 1 else 0


def ns(number, dice):
    return sum(x for x in dice if x == number)


def big_straight(dice):
    return 30 if set(dice) == {2,3,4,5,6} else 0


def full_house(dice):
    count = Counter(dice)
    return sum(dice) if set(count.values()) == {3, 2} else 0


def four_of_a_kind(dice):
    count = Counter(dice)
    number, count = count.most_common()[0]
    return number * 4 if count >= 4 else 0


def little_straight(dice):
    return 30 if set(dice) == {1,2,3,4,5} else 0


funcs = [
    yacht,
    partial(ns, 1),
    partial(ns, 2),
    partial(ns, 3),
    partial(ns, 4),
    partial(ns, 5),
    partial(ns, 6),
    full_house,
    four_of_a_kind,
    little_straight,
    big_straight,
    sum,
]

def score(dice, category):
    try:
        return funcs[category](dice)
    except IndexError:
        raise ValueError(f"No such category {category}")