def find_smallest_set_of_vertices(n: int, edges: list) -> list:
    """
    Finds the smallest set of vertices
    """
    in_degrees = [0] * n

    for _, dest in edges:
        in_degrees[dest] += 1

    result = [idx for idx, degree in enumerate(in_degrees) if degree == 0]
    return result
