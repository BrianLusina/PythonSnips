from typing import List, TypeVar

T = TypeVar("T")


def intersect(list_one: List[T], list_two: List[T], include_duplicates: bool = True) -> List[T]:
    """
    Given two arrays, find their intersection. This assumes that the lists are not sorted. First sorting takes place
    on both lists which will incur a cost of O(nlog(n)) + O(mlog(m)) depending on the algorithm used. Time will also
    include iterating over both lists which will be O(n+m) where n is the size of list one and m is the size of list two
    Next 2 pointers are set to be used to keep track of which element we are on in the iteration of both lists.
    As long as both pointers are less than their respective lists, we compare each element to each other. If the element
    from the first collection/list is less than an element from the second collection, we move the first pointer a step
    forward, otherwise we move the second pointer.
    In the event, they are equal to each other, it means there is an intersection. At this point we check if the
    include_duplicates argument is true and include the first element. If it is set to false, we check if the preceding
    element from the first list is not equal to the current element and include it, this removes duplicates.
    Afterwards, we move the pointers forward.

    Space Complexity results in O(n+m) were n is the size of list one and m is the size of list two. This is because
    the elements are stored in a resulting list which is returned as the result of this function.
    """
    sorted_list_one, sorted_list_two, result = sorted(list_one), sorted(list_two), []
    pointer_one, pointer_two = 0, 0

    while pointer_one < len(sorted_list_one) and pointer_two < len(sorted_list_two):
        first_element = sorted_list_one[pointer_one]
        second_element = sorted_list_two[pointer_two]

        if first_element < second_element:
            pointer_one += 1
        elif second_element < first_element:
            pointer_two += 1
        else:
            if include_duplicates:
                result.append(first_element)
            else:
                if pointer_one == 0 or first_element != sorted_list_one[pointer_one - 1]:
                    result.append(first_element)
            pointer_one += 1
            pointer_two += 1
    return result
