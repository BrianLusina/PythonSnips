import unittest
from . import num_similar_groups, num_similar_groups_2


class SimilarStringGroupsTestCase(unittest.TestCase):
    def test_1(self):
        strs = ["jhki", "kijh", "jkhi", "kihj", "ijhk"]
        expected = 3
        actual = num_similar_groups(strs)
        self.assertEqual(expected, actual)

    def test_2(self):
        strs = ["abc", "acb", "bac", "bca", "cab", "cba"]
        expected = 1
        actual = num_similar_groups(strs)
        self.assertEqual(expected, actual)

    def test_3(self):
        strs = ["abcd", "abdc", "acbd", "bdca"]
        expected = 2
        actual = num_similar_groups(strs)
        self.assertEqual(expected, actual)

    def test_4(self):
        strs = [
            "fgtdvepeqcfajhlzkwlpuhrwfcueqfbs",
            "fgcdvppeqcfajhlzkwluehrwftuefqbs",
            "fgtdvepeqcfajhlzkwlpuhrwfcuefqbs",
            "fgcdvepeqcfajhlzkwluphrwftuefqbs",
            "fgldvepeqcfajhlzkwcuphrwftuefqbs",
            "fgtdvefeqcpajhlzkwlpuhrwfcuefqbs",
        ]
        expected = 2
        actual = num_similar_groups(strs)
        self.assertEqual(expected, actual)


class SimilarStringGroups2TestCase(unittest.TestCase):
    def test_1(self):
        strs = ["jhki", "kijh", "jkhi", "kihj", "ijhk"]
        expected = 3
        actual = num_similar_groups_2(strs)
        self.assertEqual(expected, actual)

    def test_2(self):
        strs = ["abc", "acb", "bac", "bca", "cab", "cba"]
        expected = 1
        actual = num_similar_groups_2(strs)
        self.assertEqual(expected, actual)

    def test_3(self):
        strs = ["abcd", "abdc", "acbd", "bdca"]
        expected = 2
        actual = num_similar_groups_2(strs)
        self.assertEqual(expected, actual)

    def test_4(self):
        strs = [
            "fgtdvepeqcfajhlzkwlpuhrwfcueqfbs",
            "fgcdvppeqcfajhlzkwluehrwftuefqbs",
            "fgtdvepeqcfajhlzkwlpuhrwfcuefqbs",
            "fgcdvepeqcfajhlzkwluphrwftuefqbs",
            "fgldvepeqcfajhlzkwcuphrwftuefqbs",
            "fgtdvefeqcpajhlzkwlpuhrwfcuefqbs",
        ]
        expected = 2
        actual = num_similar_groups_2(strs)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
