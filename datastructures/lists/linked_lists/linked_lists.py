from datastructures.lists.linked_lists.build_one_2_3 import build_one_two_three
from datastructures.lists.linked_lists.singly_linked_list import SinglyLinkedList

myArray = ["Dad", "Mom", "Linda", "Joyce", "Brian", "Mideva", "Lucky", "Fox", "Junior", "Coco", "Rabbits"]

# example code
single_list = SinglyLinkedList()
# double_list = DoublyLinkedList()
# circular_list = CircularLinkedList()

for x in range(0, len(myArray)):
    single_list.push(myArray[x])


#
# for x in range(0, len(myArray)):
#     double_list.push(myArray[x])
#
# # single_list.display()
# double_list.display()
#
# # single_list.delete_node("Rabbits")
# double_list.delete_node("Rabbits")
#
# # single_list.display()
# double_list.display()

# double_list.delete_node(double_list.search('b'))


def length(node):
    if not node:
        return 0
    else:
        return 1 + length(node.next)


def count(node, data):
    """
    Counts the number of occurrences of data in a node
    :param node: Node object
    :param data: Data to count
    :return: Number of occurrences of data in a node
    """
    if not node:
        return 0
    else:
        number = 0
        while node:
            if node.data == data:
                number += 1
            node = node.next
        return number


if __name__ == "__main__":
    build = build_one_two_three()

    print(length(build))
    print(count(build, 3))
