from typing import List


def dynamic_array(n: int, queries: List[List[int]]) -> List[int]:
    last_answer = 0
    arr = [[] for _ in range(n)]
    answers = []

    for query in queries:
        query_type, x, y = query

        if query_type == 1:
            idx = (x ^ last_answer) % n
            arr[idx].append(y)
        if query_type == 2:
            idx = (x ^ last_answer) % n
            last_answer = arr[idx][y % len(arr[idx])]
            answers.append(last_answer)

    return answers
