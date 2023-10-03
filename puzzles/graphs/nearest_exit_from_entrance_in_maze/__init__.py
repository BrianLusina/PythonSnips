from typing import List, Tuple, Deque, Set
from collections import deque


def nearest_exit(maze: List[List[str]], entrance: List[int]) -> int:
    """Finds the minimum number of steps to get from the entrance to the exit in a maze
    Args:
        maze(list): maze represented by a 2D array with + as walls and `.` as empty spots
        entrance(list): position of entrance(or starting point)
    Returns:
        int: minimum number of steps from entrance
    """
    # directions to move along the x-axis & y-axis, or left to right and vice versa
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    entrance = (entrance[0], entrance[1])
    queue = deque([entrance])
    visited = set()
    visited.add(entrance)
    step = 0

    while queue:
        step_length = len(queue)
        for i in range(step_length):  # here, we can use length of the deque to iterate through level by level
            node = queue.popleft()
            if node[0] == 0 or node[0] == len(maze) - 1 or node[1] == 0 or node[1] == len(maze[0]) - 1:
                if maze[node[0]][node[1]] == '.' and (node[0], node[1]) != entrance:
                    return step
            for d in directions:
                newD = (node[0] + d[0], node[1] + d[1])
                if newD not in visited and 0 <= newD[0] < len(maze) and 0 <= newD[1] < len(maze[0]) and maze[newD[0]][
                    newD[1]] == '.':  # only add valid nodes to the queue!
                    visited.add(newD)  # mark it as visited, so we don't loop forever
                    queue.append(newD)
        step += 1  # after we finish with a level, increment step by one
    return -1
