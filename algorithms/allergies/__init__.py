class Allergies(object):
    ALLERGY_SCORES = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        if score is None or not isinstance(score, int):
            raise TypeError("Score must be an integer")
        self.score = score

    def is_allergic_to(self, allergen):
        """
        Checks if Tom is allergic to this particular allergen. Does a bitwise AND to perform the check
        :param allergen: the allergen to check for
        :return: True/False if Tom is allergic
        :rtype: bool
        """
        return self.ALLERGY_SCORES[allergen] & self.score

    def allergies(self):
        """
        Sorts the list of allergies in alphabetic order and returns them
        :return: a sorted list of all the allergies
         :rtype: list
        """
        return sorted(list(allergy for allergy in self.ALLERGY_SCORES if
                           self.is_allergic_to(allergy)))
