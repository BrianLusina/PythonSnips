import unittest
from . import max_score


class MaximalScoreAfterKOperationsTestCase(unittest.TestCase):
    def test_1(self):
        nums = [10,20,30,40,50]
        k = 4
        expected = 140
        actual = max_score(nums, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [5,12,7,3,10]
        k = 3
        expected = 29
        actual = max_score(nums, k)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [6,9,15]
        k = 2
        expected = 24
        actual = max_score(nums, k)
        self.assertEqual(expected, actual)

    def test_4(self):
        nums = [1,10,3,3,3]
        k = 3
        expected = 17
        actual = max_score(nums, k)
        self.assertEqual(expected, actual)

    def test_5(self):
        nums = [7,10,16]
        k = 2
        expected = 26
        actual = max_score(nums, k)
        self.assertEqual(expected, actual)

    def test_6(self):
        nums = [5,120,7,30,10]
        k = 3
        expected = 190
        actual = max_score(nums, k)
        self.assertEqual(expected, actual)

    def test_7(self):
        nums = [100,200,300,400,500]
        k = 4
        expected = 1400
        actual = max_score(nums, k)
        self.assertEqual(expected, actual)

    def test_8(self):
        nums = [20,20,20,20]
        k = 3
        expected = 60
        actual = max_score(nums, k)
        self.assertEqual(expected, actual)

    def test_9(self):
        nums = [81698,68947,77662,46592,13226,37325,2800,22504,99833,77083,38068,40934,3640,33631,84634,66457,21309,
                64949,94392,3553,68692,31662,17348,42805,32143,7099,88341,65391,8164,65035,22205,88755,80232,84970,
                19213,36774,33975,47386,74761,4893,9040,8263,60379,88511,49040,89068,72601,17683,17871,46156,2805,10247,
                54658,27427,51671,81935,59171,70215,56400,83874,9230,31194,98266,84404,1200,89589,70329,39209,19461,
                19022,86927,26496,27561,96403,78150,47498,5696,78065,75672,44842,64855,19760,57351,7788,41209,89214,
                24315,6398,60738,88636,71885,44987,28782,13700,78965,47534,82496,66162,89596,3646,73107,13112,28574,
                37445,14997,98860]
        k = 1000
        expected = 7709375
        actual = max_score(nums, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
