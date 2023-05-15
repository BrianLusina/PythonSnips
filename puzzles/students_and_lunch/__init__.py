from typing import List
from collections import deque


def count_students(students: List[int], sandwiches: List[int]) -> int:
    """
    Counts the number of students unable to eat given their preferences in a list of integers to the stack of sandwiches
    in the sandwiches list.

    Complexity Analysis:
        Time Complexity: O(n) where n is the size of the student list. We iterate over the student queue to match the
        student preference to the sandwich in the stack.

        Space Complexity: O(n + m) where n is the size of the students list and m is the size of the sandwich stack.
        We store the students queue & sandwich stack in separate deque in order to keep track of the items to perform
        comparisons, this means the original inputs are not modified in place.
    @param students: list of students and their sandwich preferences
    @param sandwiches: list of types of sandwiches
    @return: count of students unable to eat
    """
    student_queue = deque(students)
    sandwich_stack = deque(sandwiches)
    number_of_matches = len(student_queue)

    # while we still have students in the queue
    while len(student_queue) > 0 and number_of_matches > 0:
        # if the first student in the queue likes the sandwich at the top of the stack
        if student_queue[0] == sandwich_stack[0]:
            # we remove the student and the sandwich from the front of the queue and the top of the stack respectively
            student_queue.popleft()
            sandwich_stack.popleft()
            number_of_matches = len(student_queue)
        else:
            # we move the student to the back of the stack if they don't like the sandwich
            student_pref = student_queue.popleft()
            student_queue.append(student_pref)
            number_of_matches -= 1

    # return the number of students left in the queue
    return len(student_queue)
