import unittest

from puzzles.rectangles import count


class WordTest(unittest.TestCase):
    # unit tests
    @staticmethod
    def test_zero_area_1():
        assert 0 == count()

    @staticmethod
    def test_zero_area_2():
        lines = ""
        assert 0 == count(lines)

    @staticmethod
    def test_empty_area():
        lines = " "
        assert 0 == count(lines)

    @staticmethod
    def test_one_rectangle():
        lines = ["+-+",
                 "| |",
                 "+-+",
                 ]
        assert 1 == count(lines)

    @staticmethod
    def test_two_rectangles_no_shared_parts():
        lines = ["  +-+",
                 "  | |",
                 "+-+-+",
                 "| |  ",
                 "+-+  "
                 ]
        assert 2 == count(lines)

    @staticmethod
    def test_five_rectangles_three_regions():
        lines = ["  +-+",
                 "  | |",
                 "+-+-+",
                 "| | |",
                 "+-+-+"
                 ]
        assert 5 == count(lines)

    @staticmethod
    def test_incomplete_rectangles():
        lines = ["  +-+",
                 "    |",
                 "+-+-+",
                 "| | -",
                 "+-+-+"
                 ]
        assert 1 == count(lines)

    @staticmethod
    def test_complicated():
        lines = ["+------+----+",
                 "|      |    |",
                 "+---+--+    |",
                 "|   |       |",
                 "+---+-------+"
                 ]
        assert 3 == count(lines)

    @staticmethod
    def test_not_so_complicated():
        lines = ["+------+----+",
                 "|      |    |",
                 "+------+    |",
                 "|   |       |",
                 "+---+-------+"
                 ]
        assert 2 == count(lines)


if __name__ == '__main__':
    unittest.main()
