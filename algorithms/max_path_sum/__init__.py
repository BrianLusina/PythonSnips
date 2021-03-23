"""
Finds the maximum path sum in a given triangle of numbers
"""


def max_path_sum_in_triangle(triangle):
    """
    Finds the maximum sum path in a triangle(tree) and returns it
    :param triangle:
    :return: maximum sum path in the given tree
    :rtype: int
    """
    length = len(triangle)

    for _ in range(length - 1):
        a = triangle[-1]
        b = triangle[-2]

        for y in range(len(b)):
            b[y] += max(a[y], a[y + 1])

        triangle.pop(-1)
        triangle[-1] = b

    return triangle[0][0]


if __name__ == "__main__":
    triangle_1 = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]

    print(f"Maximum path sum in {triangle_1} is {max_path_sum_in_triangle(triangle_1)}")

    with open("triangle.txt", "r") as numbers:
        triangle_2 = []
        for line in numbers:
            k = [int(x) for x in line.split(" ")]
            triangle_2.append(k)

    print(f"Maximum path sum in {triangle_2} is {max_path_sum_in_triangle(triangle_2)}")
