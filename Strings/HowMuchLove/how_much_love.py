"""
if the number of petals is greater than the length of the list, reduce the number of petals by the length

loop though list, checking if the number of petals is greater than the length of the list
reduce the number of petals by the length of the list after every iteration until the number is less than or equal to
length of the list, in this case: it is either 1-6
return the value at that index
"""


def how_much_i_love_you(nb_petals):
    love = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    while nb_petals > len(love):
        nb_petals -= len(love)
        if nb_petals in range(0, len(love)):
            break
        else:
            continue

    return love[nb_petals - 1]


def how_much_i_love_you_2(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]
