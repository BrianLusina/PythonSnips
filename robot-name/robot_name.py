from random import sample
from string import ascii_uppercase


class Robot(object):

    def __init__(self):
        self._name = None
        self._past_names = set()

    def letters(self):
        return "".join(sample(ascii_uppercase, 2))

    def numbers(self):
        return "".join(str(x) for x in sample(range(0, 10), 3))

    def generate_name(self):
        if not self._name:
            # collision detected
            while True:
                self._name = self.letters() + self.numbers()
                if self._name not in self._past_names:
                    self._past_names.add(self._name)
                    break
        return self._name

    def del_name(self):
        self._name = None

    name = property(generate_name, None, del_name)

    def reset(self):
        del self.name
