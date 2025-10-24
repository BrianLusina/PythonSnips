from typing import Union


def bouncing_ball(
    h: Union[int, float], bounce: float, window: Union[int, float]
) -> int:
    seen_count = -1
    if 0 < bounce < 1:
        while h > window:
            h *= bounce
            seen_count += 2

    return seen_count
