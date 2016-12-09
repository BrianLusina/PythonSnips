class Animal(object):
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def speak(self):
        return self.name + " meows."

cat = Cat("Mr Whiskers")
print(cat.speak())
print(isinstance(cat, Animal))
