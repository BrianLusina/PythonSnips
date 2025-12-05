import unittest
from typing import List
from parameterized import parameterized
from pystrings.longest_common_prefix import longest_common_prefix


class LongestCommonPrefixTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
            (["a"], "a"),
            (["interspecies", "interstellar", "interstate"], "inters"),
            (["cir", "car"], "c"),
            (["dna"], "dna"),
            (["chlorine", "oxygen", "carbon"], ""),
            (["carpenter", "car", "carpet"], "car"),
        ]
    )
    def test_longest_common_prefix(self, strs: List[str], expected: str):
        actual = longest_common_prefix(strs)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
