from collections import defaultdict


class School(object):

    def __init__(self, name):
        self.name = name
        self.database = defaultdict(set)

    def grade(self, grade):
        return self.database[grade]

    def add(self, student_name, grade):
        return self.database[grade].add(student_name)

    def sort(self):
        return sorted((grade, tuple(sorted(students))) for grade, students in self.database.items())
