import unittest

from datastructures.linked_lists.build_one_2_3 import push, build_one_two_three, Node


class BuildOneTwoThreeTestCases(unittest.TestCase):
    def test_create_new_linked_list_with_push(self):
        self.assertEqual(push(None, 1).data, 1, "Should be able to create a new linked list with push().")
        self.assertEqual(push(None, 1).next, None, "Should be able to create a new linked list with push().")
        self.assertEqual(push(Node(1), 2).data, 2, "Should be able to prepend a node to an existing node.")
        self.assertEqual(push(Node(1), 2).next.data, 1, "Should be able to prepend a node to an existing node.")
        self.assertEqual(build_one_two_three().data, 1, "First node should should have 1 as data.")
        self.assertEqual(build_one_two_three().next.data, 2, "First node should should have 1 as data.")
        self.assertEqual(build_one_two_three().next.next.data, 3, "Second node should should have 2 as data.")
        self.assertEqual(build_one_two_three().next.next.next, None, "Third node should should have 3 as data.")


if __name__ == '__main__':
    unittest.main()
