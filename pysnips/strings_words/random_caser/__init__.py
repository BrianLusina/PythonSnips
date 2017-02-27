from random import choice


def random_case(sentence):
    """
    Randomly changes the case of the input sentence
    :param sentence: the sentence to randomly change case
    :return: a new string with the cases randomly swapped
    :rtype: str
    """
    return "".join(choice([let.upper(), let.lower()]) for let in sentence)
