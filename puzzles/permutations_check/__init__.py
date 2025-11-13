from typing import List


def check(n: int, m: int, games: List[List[int]]) -> bool:
    pairs = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]

    for game_round in games:
        for i, j in pairs:
            if i in game_round[: n // 2] and j in game_round[: n // 2]:
                return False

            if i in game_round[n // 2 :] and j in game_round[n // 2 :]:
                return False

    return True
