from data_structures.lists.linked_lists import LinkedList
from data_structures.lists.linked_lists.circular_linked_list import CircularLinkedList
from data_structures.lists.linked_lists.doubly_linked_list import DoublyLinkedList
from data_structures.lists.linked_lists.singly_linked_list import SinglyLinkedList

myArray = ["Dad", "Mom", "Linda", "Joyce", "Brian", "Mideva", "Lucky", "Fox", "Junior", "Coco", "Rabbits"]

# example code
single_list = SinglyLinkedList()

for x in range(0, len(myArray)):
    single_list.add(myArray[x])

single_list.display()

single_list.delete_node("Rabbits")

single_list.display()

# double_list.delete_node(double_list.search('b'))
