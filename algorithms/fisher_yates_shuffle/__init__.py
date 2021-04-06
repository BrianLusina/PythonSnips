"""
Small demonstration on fisher yates algorithm
"""
import random


def get_random(floor, ceiling):
    """
    Gets a random number between floor and ceiling
    :rerturn: randomly selected element in the range
    """
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    """
    Shuffles a list in_place, this means that the input list is destroyed
    Does not return anything, as the input list is destroyed and thus will be altered. Be careful
    when using this function, it has side-effects
    :param: the_list list being used to shuffle
    :return: None or the list itself if the list is length of 0 or 1
    :rtype: None
    """
    # if the list is 0 or 1 in length, simply return it
    if len(the_list) <= 1:
        return the_list

    last_index_in_list = len(the_list) - 1

    # walk through the list from beginning to end
    for index_we_are_choosing in range(0, last_index_in_list):
        # choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # must be an item AFTER the current item, because the stuff
        # before has all already been placed

        random_choice_index = get_random(index_we_are_choosing, last_index_in_list)

        # place our random choice in the spot by swapping
        if random_choice_index != index_we_are_choosing:
            the_list[index_we_are_choosing], the_list[random_choice_index] = \
                the_list[random_choice_index], the_list[index_we_are_choosing]
