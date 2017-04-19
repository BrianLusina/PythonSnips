grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


# function to display the grades individually
def print_grades(grades):
    for grade in grades:
        print(grade)


# function to calculate the sum of the grades
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total


# function to calculate the average
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average


# function to calculate the variance
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += ((average - score) ** 2) / len(scores)
    return variance


# function to calculate the standard deviation of the grades list
def grades_std_deviation(variance):
    return variance ** 0.5


print(grades)
