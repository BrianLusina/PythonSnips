def sqrt_estimate(x: int) -> int:
    left = 0
    right = x
    result = 0

    while left <= right:
        mid = left + (right - left) // 2
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared < x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result
