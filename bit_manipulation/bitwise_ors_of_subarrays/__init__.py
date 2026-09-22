def subarray_bitwise_ors(arr: list[int]) -> int:
    result = set()
    current = {0}
    for x in arr:
        current = {x | y for y in current} | {x}
        result |= current
    return len(result)


def subarray_bitwise_ors_2(arr: list[int]) -> int:
    all_ors_set = set()  # store all distinct OR results seen so far
    prev_ors_set = set()  # store distinct ORs of subarrays ending at previous index

    for num in arr:  # iterate through array
        curr_ors_set = {
            num
        }  # ORs of subarrays ending here (start new subarray at this element)
        for (
            val
        ) in prev_ors_set:  # extend all previous-ending subarrays by current element
            curr_ors_set.add(val | num)  # update OR result
        all_ors_set |= curr_ors_set  # merge into global distinct set
        prev_ors_set = curr_ors_set  # move window of tracked ORs forward

    return len(all_ors_set)  # count distinct OR values
