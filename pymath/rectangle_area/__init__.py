def compute_area(
    ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int
):
    # 1. Calculate the area of each individual rectangle
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)

    # 2. Calculate the area of the overlap (A intersect B)

    # Determine the coordinates of the overlap rectangle: (ix1, iy1) to (ix2, iy2)

    # The left edge of the overlap is the max of the two left edges
    ix1 = max(ax1, bx1)
    # The right edge of the overlap is the min of the two right edges
    ix2 = min(ax2, bx2)

    # The bottom edge of the overlap is the max of the two bottom edges
    iy1 = max(ay1, by1)
    # The top edge of the overlap is the min of the two top edges
    iy2 = min(ay2, by2)

    # Calculate the width and height of the overlap
    overlap_width = max(0, ix2 - ix1)
    overlap_height = max(0, iy2 - iy1)

    # The max(0, ...) ensures that if the rectangles do not overlap
    # (e.g., ix2 < ix1), the width/height is 0, and the overlap_area is 0.
    overlap_area = overlap_width * overlap_height

    # 3. Apply the Inclusion-Exclusion Principle
    total_area = area_a + area_b - overlap_area

    return total_area
