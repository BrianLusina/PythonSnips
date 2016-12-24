from data_structures.lists.linked_lists import LinkedList
from data_structures.lists.linked_lists.circular_linked_list import CircularLinkedList
from data_structures.lists.linked_lists.doubly_linked_list import DoublyLinkedList
from data_structures.lists.linked_lists.singly_linked_list import SinglyLinkedList

myArray = ["Dad", "Mom", "Linda", "Joyce", "Brian", "Mideva", "Lucky", "Fox", "Junior", "Coco", "Rabbits"]

for x in range(0, len(myArray)):
    double_list = DoublyLinkedList(myArray[x])
    double_list.next = myArray[x]

print(double_list)

