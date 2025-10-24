import unittest

from . import find_max_length


class MaxLengthContiguousBinarySubArrayTestCases(unittest.TestCase):
    def test_0(self):
        nums = [0]
        expected = 0
        actual = find_max_length(nums)
        self.assertEqual(expected, actual)

    def test_0_1(self):
        nums = [0, 1]
        expected = 2
        actual = find_max_length(nums)
        self.assertEqual(expected, actual)

    def test_0_1_0(self):
        nums = [0, 1, 0]
        expected = 2
        actual = find_max_length(nums)
        self.assertEqual(expected, actual)

    def test_0_1_0_0_1_1_0(self):
        nums = [0, 1, 0, 0, 1, 1, 0]
        expected = 6
        actual = find_max_length(nums)
        self.assertEqual(expected, actual)

    def test_1_1_0_1_1_0_1_1_returns_4(self):
        """Should return 4 for binary array of [1,1,0,1,1,0,1,1]"""
        nums = [1, 1, 0, 1, 1, 0, 1, 1]
        expected = 4
        actual = find_max_length(nums)
        self.assertEqual(expected, actual)

    def test_0_1_1_0_1_1_1_0_0_0_returns_10(self):
        """Should return 10 for binary array of [0, 1, 1, 0, 1, 1, 1, 0, 0, 0]"""
        nums = [0, 1, 1, 0, 1, 1, 1, 0, 0, 0]
        expected = 10
        actual = find_max_length(nums)
        self.assertEqual(expected, actual)

    def test_0_0_1_1_1_0_0_0_0_0_returns_6(self):
        """Should return 6 for binary array of [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]"""
        nums = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
        expected = 6
        actual = find_max_length(nums)
        self.assertEqual(expected, actual)


@test.describe("Random Tests")
def tests():
    def check(s) -> int:
        Track, balance, index, len1 = {}, 0, 0, 0
        for i in s:
            if i == 0:
                balance -= 1
            if i == 1:
                balance += 1
            if balance in Track:
                Track[balance].append(index)
            else:
                Track[balance] = [index]
            index += 1
        for i in Track:
            if len(Track[i]) >= 2:
                len1 = max(len1, max(Track[i]) - min(Track[i]))
            if i == 0:
                len1 = max(len1, max(Track[0]) + 1)
        return len1

    randomizer = lambda: random.seed(random.choice(range(4, 12)))

    rnd1 = lambda m: [random.choices([0, 1], [20, 80])[0] for _ in range(m)]
    rnd2 = lambda m: [random.choices([0, 1], [50, 50])[0] for _ in range(m)]
    rnd3 = lambda m: [random.choices([0, 1], [80, 20])[0] for _ in range(m)]

    def shuffs(s):
        shuffle(s)
        answer = check(s)
        test.assert_equals(binarray(s.copy()), answer)

    def rnd_tests(title, l, m, flag):
        @test.it(title + " size")
        def _():
            for _ in range(l):
                if flag:
                    s = random.choice([rnd1, rnd2, rnd3])(m)
                else:
                    s = [random.choice([0, 1]) for _ in range(m)]
                answer = check(s)
                test.assert_equals(binarray(s.copy()), answer)
                if flag:
                    shuffs(s)

    for title, rang, size, flag in [
        ("Small", 10, 50, True),
        ("Big", 30, 100, True),
        ("Very Big", 30, 1_20_000, False),
    ]:
        if random.choice([0, 1]):
            randomizer()
        rnd_tests(title, rang, size, flag)


if __name__ == "__main__":
    unittest.main()
