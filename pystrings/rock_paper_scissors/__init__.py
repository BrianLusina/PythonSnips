mapping = {
    "scissors": "paper",
    "paper": "rock",
    "rock": "scissors",
}


def rps(p1: str, p2: str) -> str:
    if p1 == p2:
        return "Draw!"
    if mapping[p1] == p2:
        return "Player 1 won!"
    return "Player 2 won!"
