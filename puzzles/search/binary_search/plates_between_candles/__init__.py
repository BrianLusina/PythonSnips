from typing import List


def plates_between_candles(plates_and_candles: str, queries: List[List[int]]) -> List[int]:
    """Finds the number of plates between candles on a table represented by a string where a plate is * and a candle is |
    Args:
        plates_and_candles (str): table representing the plates and candles.
        queries (List[List[int]]): queries representing the queries between certain indices on the table
    Returns:
        List[int]: number of plates between candles in the queries. Rather answer to each query
    """
    # This will hold the indices of candles in the plates and candles
    # This allows us to do basic arithmetic on the indices to find the number of plates.
    # also we perform a binary search on this candle list. We find the left_pos and right_pos indicating the outside
    # candles positions in the input. Then, We know that the number of plates is given by the interval between the two
    # bounding candles subtracted by the number of candles in between. With the indices left_pos and right_pos, we can
    # derive the number of plates to be (candles[right_pos] - candles[left_pos]) - (right_pos - left_pos).
    # space complexity is O(c) where c is the number of candles. The worst case is that there are all candles.
    candles = []

    # Adds all candle indices on the table to the candle list.
    # Time Complexity is O(n) where n is the number of candles and plates. We have to scan over all plates and candles
    # to check which is a candle before adding its index.
    for i in range(len(plates_and_candles)):
        if plates_and_candles[i] == "|":
            candles.append(i)

    # our result list will store answers to each query
    result = []

    for q_left, q_right in queries:
        left_pos, right_pos = -1, -1

        # 1. find the index of the first candle that comes after q_left
        # the index left_pos in candles of the first candle that is greater than q_left means that whenever
        # candles[index] >= q_left, we can update left_pos until we find the leftmost index at candles[index] >= q_left
        # (recurse on left-half).
        left, right = 0, len(candles) - 1
        while left <= right:
            mid = (left + right) // 2
            if candles[mid] >= q_left:
                right = mid - 1
                left_pos = mid
            else:
                left = mid + 1

        # 2. Find the index of the last candle that comes before q_right
        # The index right_pos in candles of the last candle that is smaller than q_right means that whenever
        # candles[index] <= q_right, we can update right_pos until we find the rightmost index
        # at candles[index] >= q_right (recurse on right-half).
        left, right = 0, len(candles) - 1
        while left <= right:
            mid = (left + right) // 2
            if candles[mid] <= q_right:
                left = mid + 1
                right_pos = mid
            else:
                right = mid - 1

        # result = range between two outermost candles - candle count in between
        if (left_pos != -1) and (right_pos != -1) and (right_pos > left_pos):
            number_of_plates = candles[right_pos] - candles[left_pos] - (right_pos - left_pos)
            result.append(number_of_plates)
        else:
            result.append(0)

    return result
