class Garden(object):
    STUDENTS = ["Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"]

    __PLANTS = {"C": "Clover", "G": "Grass",
                "R": "Radishes", "V": "Violets"}

    def __init__(self, plant_diagram, students=None):
        self.plant_diagram = plant_diagram.split()
        if students:
            self.students = sorted(students)
        else:
            self.students = self.STUDENTS

    def plants(self, student):
        start = self.students.index(student) * 2
        slot = slice(start, start + 2)
        return [self.__PLANTS[plant]
                for plant in (self.plant_diagram[0][slot] +
                              self.plant_diagram[1][slot])]
