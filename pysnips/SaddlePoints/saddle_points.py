def saddle_points(matrix):
    if not matrix:
        return set()
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Irregular matrices are not allowed")
    # gets the maximum val per row
    mmax = [max(row) for row in matrix]
    # gets the min value per col
    mmin = [min(col) for col in zip(*matrix)]
    points = [(i, j) for i in range(len(matrix))
              for j in range(len(matrix[0])) if mmax[i] == mmin[j]]

    return set(points)
