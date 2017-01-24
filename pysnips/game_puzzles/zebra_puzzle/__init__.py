"""This solution for the Zebra Puzzle is adapted from a solution
by Peter Norvig for the course "Design of Computer Programs" on Udacity.
https://www.udacity.com/course/cs212
"""
from itertools import permutations


def just_right_of(x, y):
    return x - y == 1


def next_to(x, y):
    return abs(x - y) == 1


def solution():
    # create a range from 0, 4, map the outputs to variables and the variables to houses, which is now a tuple
    # this will be the positions of the houses
    houses = first, _, middle, _, _ = range(5)

    # produce all the possible orderings of the houses as a list, as we can not know which house is positioned where
    # from any point of observation
    orderings = list(permutations(houses))

    result = next([{Englishman: "Englishman", Spaniard: "Spaniard",
                    Ukranian: "Ukranian", Japanese: "Japanese",
                    Norwegian: "Norwegian"}[x]
                   for x in (water, zebra)]
                  for (red, green, ivory, yellow, blue) in orderings
                  if just_right_of(green, ivory)
                  for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                  if Englishman is red
                  if Norwegian is first
                  if next_to(Norwegian, blue)
                  for (coffee, tea, milk, oj, water) in orderings
                  if coffee is green
                  if Ukranian is tea
                  if milk is middle
                  for (OldGold, kools, Chesterfields, Luckystrike, Parliament) in orderings
                  if kools is yellow
                  if Luckystrike is oj
                  if Japanese is Parliament
                  for (dog, snails, fox, horse, zebra) in orderings
                  if Spaniard is dog
                  if OldGold is snails
                  if next_to(Chesterfields, fox)
                  if next_to(kools, horse)
                  )
    return "It is the {} who drinks the water.\nThe {} keeps the zebra.".format(*result)
