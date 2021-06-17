import unittest

from design_patterns.orderedstream import OrderedStream


class OrderedStreamTestCase(unittest.TestCase):
    def test_inserts(self):
        n = 5
        ordered_stream = OrderedStream(n)

        insert_3 = ordered_stream.insert(3, "ccccc")
        self.assertEqual([], insert_3)

        insert_1 = ordered_stream.insert(1, "aaaaa")
        self.assertEqual(["aaaaa"], insert_1)

        insert_2 = ordered_stream.insert(2, "bbbbb")
        self.assertEqual(["bbbbb", "ccccc"], insert_2)

        insert_5 = ordered_stream.insert(5, "eeeee")
        self.assertEqual([], insert_5)

        insert_4 = ordered_stream.insert(4, "ddddd")
        self.assertEqual(["ddddd", "eeeee"], insert_4)


if __name__ == '__main__':
    unittest.main()
