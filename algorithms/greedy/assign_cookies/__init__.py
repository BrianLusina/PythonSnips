from typing import List


def find_content_children(greeds: List[int], cookies: List[int]) -> int:
    # This in-place sorting of both g and s results in a time complexity of O(n log(n) + m log(m))
    greeds.sort()
    cookies.sort()

    cookie, greed = 0, 0
    count = 0

    # We iterate through each greed factor and cookie
    while greed < len(greeds) and cookie < len(cookies):
        # When we get a cookie that satisfies kid i, we assign that cookie to the child
        # and move along, increasing the count as well
        if cookies[cookie] >= greeds[greed]:
            count += 1
            greed += 1
        cookie += 1

    return count
