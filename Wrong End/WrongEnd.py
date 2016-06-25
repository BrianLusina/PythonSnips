"""
You're at the zoo... all the meerkats look weird. Something has gone terribly wrong - someone has gone and switched their heads and tails around!

Save the animals by switching them back. You will be given an array which will have three values (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).

Same goes for all the other arrays/lists that you will get in the tests: you have to change the element positions with the same exact logics - simples!
"""

class WrongEnd(object):
    def __init__(self,meerkat):
        self.meerkat = meerkat
        
    @staticmethod        
    def fix_the_meerkat(arr):
        return list(reversed(arr))

class Test(object):
    def __init__(self,n):
        self.n = n

    @staticmethod
    def test_function(actual,expected):
        return "Test for " + str(actual) + " passed " if actual == expected else "Test for " + str(actual) + " failed, expected " + str(expected)


print Test.test_function(WrongEnd.fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
print Test.test_function(WrongEnd.fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])
print Test.test_function(WrongEnd.fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])
print Test.test_function(WrongEnd.fix_the_meerkat(["lower legs", "torso", "upper legs"]), ["upper legs", "torso", "lower legs"])
print Test.test_function(WrongEnd.fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])