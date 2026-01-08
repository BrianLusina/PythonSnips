from typing import List, Deque, DefaultDict, Tuple
from collections import deque, defaultdict


def cat_mouse_game(graph: List[List[int]]) -> int:
    n = len(graph)

    # Final game states that determine which player wins
    draw, mouse, cat = 0, 1, 2
    color: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)

    # What nodes could play their turn to
    # arrive at node (m, c, t) ?
    def parents(m, c, t):
        if t == 2:
            for m2 in graph[m]:
                yield m2, c, 3 - t
        else:
            for c2 in graph[c]:
                if c2:
                    yield m, c2, 3 - t

    # degree[node] : the number of neutral children of this node
    degree = {}
    for m in range(n):
        for c in range(n):
            degree[m, c, 1] = len(graph[m])
            degree[m, c, 2] = len(graph[c]) - (0 in graph[c])

    # enqueued : all nodes that are colored
    queue: Deque[Tuple[int, int, int, int]] = deque([])
    for i in range(n):
        for t in range(1, 3):
            color[0, i, t] = mouse
            queue.append((0, i, t, mouse))
            if i > 0:
                color[i, i, t] = cat
                queue.append((i, i, t, cat))

    # percolate
    while queue:
        # for nodes that are colored :
        i, j, t, c = queue.popleft()
        # for every parent of this node i, j, t :
        for i2, j2, t2 in parents(i, j, t):
            # if this parent is not colored :
            if color[i2, j2, t2] == draw:
                # if the parent can make a winning move (ie. mouse to MOUSE), do so
                if t2 == c:  # winning move
                    color[i2, j2, t2] = c
                    queue.append((i2, j2, t2, c))
                # else, this parent has degree[parent]--, and enqueue if all children
                # of this parent are colored as losing moves
                else:
                    degree[i2, j2, t2] -= 1
                    if degree[i2, j2, t2] == 0:
                        color[i2, j2, t2] = 3 - t2
                        queue.append((i2, j2, t2, 3 - t2))

    return color[1, 2, 1]
