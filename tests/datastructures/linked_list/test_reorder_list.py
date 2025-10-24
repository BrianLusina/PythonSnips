import unittest
from datastructures.linked_lists.singly_linked_list import SingleNode
from datastructures.linked_lists.reorder_list import reorder_list


class ReorderListTestCase(unittest.TestCase):
    @unittest.skip(
        "Skipping due to a missing dunder method on __repr__ & __eq__ on the SingleNode class"
    )
    def test_1_2_3_4_returns_1_4_2_3(self):
        """Should return 1 -> 4 -> 2 -> 3 from 1 -> 2 -> 3 -> 4"""
        head = SingleNode(
            1, next_=SingleNode(2, next_=SingleNode(3, next_=SingleNode(4)))
        )
        expected = SingleNode(
            1, next_=SingleNode(4, next_=SingleNode(2, next_=SingleNode(3)))
        )
        reorder_list(head)
        self.assertEqual(expected, head)
        self.assertEqual(expected, head)

    @unittest.skip(
        "Skipping due to a missing dunder method on __repr__ & __eq__ on the SingleNode class"
    )
    def test_1_2_3_4_5_returns_1_5_2_4_3(self):
        """Should return 1 -> 5 -> 2 -> 4 -> 3 from 1 -> 2 -> 3 -> 4 -> 5"""
        head = SingleNode(
            1,
            next_=SingleNode(
                2, next_=SingleNode(3, next_=SingleNode(4, next_=SingleNode(5)))
            ),
        )
        expected = SingleNode(
            1,
            next_=SingleNode(
                5, next_=SingleNode(2, next_=SingleNode(4, next_=SingleNode(3)))
            ),
        )
        reorder_list(head)
        self.assertEqual(expected, head)


if __name__ == "__main__":
    unittest.main()
