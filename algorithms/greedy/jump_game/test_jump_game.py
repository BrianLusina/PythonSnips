import unittest
from typing import List
from parameterized import parameterized
from algorithms.greedy.jump_game import can_jump, jump, can_jump_2, jump_2

CAN_JUMP_TEST_DATA = [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([2, 3, 0, 1, 4], True),
    ([0], True),
    ([1, 0, 1, 0], False),
    ([4, 0, 0, 0, 1], True),
    ([2, 3, 1, 1, 9], True),
    ([4, 0, 0, 0, 4], True),
    ([1], True),
]


class CanJumpTestCase(unittest.TestCase):
    @parameterized.expand(CAN_JUMP_TEST_DATA)
    def test_can_jump(self, nums: List[int], expected: bool):
        actual = can_jump(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(CAN_JUMP_TEST_DATA)
    def test_can_jump_2(self, nums: List[int], expected: bool):
        actual = can_jump_2(nums)
        self.assertEqual(expected, actual)


JUMP_GAME_TEST_DATA = [
    ([2, 3, 1, 1, 4], 2),
    ([2, 3, 1, 1, 9], 2),
    ([3, 2, 1, 1, 4], 2),
    ([4, 0, 0, 0, 4], 1),
    ([1], 0),
]


class JumpTestCase(unittest.TestCase):
    @parameterized.expand(JUMP_GAME_TEST_DATA)
    def test_jump_game(self, nums: List[int], expected: int):
        actual = jump(nums)
        self.assertEqual(expected, actual)

    @parameterized.expand(JUMP_GAME_TEST_DATA)
    def test_jump_game_2(self, nums: List[int], expected: int):
        actual = jump_2(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
