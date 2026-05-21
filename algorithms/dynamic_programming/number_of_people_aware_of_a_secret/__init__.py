from collections import deque
from typing import Tuple, Deque


def people_aware_of_secret(n: int, delay: int, forget: int) -> int:
    mod = 10**9 + 7
    # dp[i] represents the number of people who discover the secret on day i
    dp = [0] * (n + 1)
    # Day 1: one person discovers the secret
    dp[1] = 1
    # Track the number of people currently able to share (active sharers)
    sharing = 0
    # Fill dp for each day from 2 to n
    for i in range(2, n + 1):
        # A person who discovered on day (i - delay) starts sharing today
        if i - delay >= 1:
            sharing = (sharing + dp[i - delay]) % mod
        # A person who discovered on day (i - forget) stops sharing today (they forget)
        if i - forget >= 1:
            sharing = (sharing - dp[i - forget]) % mod
        # New people who discover the secret today equals current active sharers
        dp[i] = sharing % mod
    # Sum up all people who still know the secret at end of day n
    # A person discovered on day d still knows it if d + forget > n, i.e., d > n - forget
    result = 0
    for i in range(1, n + 1):
        # Person discovered on day i forgets on day i + forget, so they know it on day n if i + forget > n
        if i + forget > n:
            result = (result + dp[i]) % mod
    return result


def people_aware_of_secret_simulation_deque(n: int, delay: int, forget: int) -> int:
    know: Deque[Tuple[int, int]] = deque([(1, 1)])
    share: Deque[Tuple[int, int]] = deque([])
    know_cnt, share_cnt = 1, 0

    for i in range(2, n + 1):
        if know and know[0][0] == i - delay:
            know_cnt -= know[0][1]
            share_cnt += know[0][1]
            share.append(know[0])
            know.popleft()
        if share and share[0][0] == i - forget:
            share_cnt -= share[0][1]
            share.popleft()
        if share:
            know_cnt += share_cnt
            know.append((i, share_cnt))
    return (know_cnt + share_cnt) % (10**9 + 7)
