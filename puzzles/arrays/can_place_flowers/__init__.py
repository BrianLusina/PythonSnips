from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    count = 0

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left_plot = (i == 0) or flowerbed[i - 1] == 0
            empty_right_plot = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

            if empty_left_plot and empty_right_plot:
                flowerbed[i] = 1
                count += 1

    return count >= n


def can_place_flowers_2(flowerbed: List[int], n: int) -> bool:
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left_plot = (i == 0) or flowerbed[i - 1] == 0
            empty_right_plot = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

            if empty_left_plot and empty_right_plot:
                flowerbed[i] = 1
                count += 1

                if count >= n:
                    return True

    return count >= n
