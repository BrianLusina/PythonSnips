class Human(object):
    """
    A Human class which describes the properties of a human being
    :__init__ initialized the number of legs,eyes, hands, etc a human usually has
    """
    walks_upright = True
    talks = True

    def __init__(self, no_legs, no_hands, no_eyes, no_mouth, nose):
        self.no_legs = no_legs
        self.no_hands = no_hands
        self.no_eyes = no_eyes
        self.no_mouth = no_mouth
        self.nose = nose

    def is_upright(self, upright=walks_upright):
        """
        :param upright: whether this human is upright, takes in a Boolean, default is True
        :return: whether this human being walks upright
        """
        self.walks_upright = upright
        return self.walks_upright

    def can_talk(self, talker_=talks):
        """
        :param talker_: talks in a Boolean, whether this human can talk, default is True
        :return:
        """
        self.talks = talker_
        return self.talks


class Person(Human):
    """
    Defines a single person class which inherits from super class Human
    """
    has_name = True

    def __init__(self, name, age, height, country, no_legs, no_hands, no_eyes, no_mouth, nose):
        # noinspection PyCompatibility
        super().__init__(no_legs, no_hands, no_eyes, no_mouth, nose)
        self.name = name
        self.age = age
        self.height = height
        self.country = country


class Students(Person):
    """
    Defines a single Student. THese are the properties of a single Student
    """

    def __init__(self, homework, quizzes, tests, name, age, height, country, no_legs, no_hands, no_eyes, no_mouth,
                 nose):
        # noinspection PyCompatibility
        super().__init__(name, age, height, country, no_legs, no_hands, no_eyes, no_mouth, nose)
        self.homework = homework
        self.quizzes = quizzes
        self.tests = tests

    def homework_average(self):
        """
        :return: homework average
        """
        return sum(self.homework) / len(self.homework)

    def quizzes_average(self):
        """
        :return: the quiz average for the student
        """
        return sum(self.quizzes) / len(self.quizzes)

    def tests_average(self):
        """
        :return: the test average
        """
        return sum(self.tests) / len(self.tests)


lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    total /= len(numbers)
    return total


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return (homework * 0.1) + (quizzes * .3) + (tests * .6)


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"


print(get_letter_grade(get_average(lloyd)))


def get_class_average(students):
    results = []

    for dict_name in students:
        for key in dict_name:
            avg = get_average(dict_name)
            results.append(avg)

    return average(results)


students = [lloyd, alice, tyler]
print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))
