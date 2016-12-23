from data_structures.lists.linked_lists import LinkedList

myArray = [3, 5, 4, 6, 2, 6, 7, 8, 9, 10, 21]

myList = LinkedList(25)
myList.build_list(myArray)
myList.print_list()
