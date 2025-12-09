from typing import List, Set, Deque


def is_valid(input_str: str) -> bool:
    """
    Check if a string has a valid parenthesis structure. Letters are ignored in validation
    """
    # count tracks the number of open parenthesis
    count = 0
    for char in input_str:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            # if the count goes to negative, we have an ')' without an open '('
            if count < 0:
                return False
    # valid only if all '(' are closed i.e. the count is 0
    return count == 0


def remove_invalid_parentheses(s: str) -> List[str]:
    # The set 'level' stores all unique strings for the current number of removals.
    # We start with the original string.
    level: Set[str] = {s}

    while True:
        valid_strings = []

        # Check all strings in the current level
        for string in level:
            if is_valid(string):
                valid_strings.append(string)

        # If we found any valid strings in this level, return them.
        # Because it's BFS, these are guaranteed to be the "minimum removals".
        if valid_strings:
            return valid_strings

        # If no valid strings found, generate the next level
        next_level: Set[str] = set()
        for string in level:
            for i in range(len(string)):
                # Only try removing parentheses, skip letters
                if string[i] in "()":
                    # Create a new string excluding the character at index i
                    new_string = string[:i] + string[i + 1 :]
                    next_level.add(new_string)

        # Move to the newly generated level
        level = next_level

        # Safety check (rare case where level becomes empty)
        if not level:
            return [""]


def remove_invalid_parentheses_2(s):
    result: Set[str] = set()

    # Step 1: Determine how many left and right parentheses need to be removed
    left_to_remove = right_to_remove = 0
    for char in s:
        if char == "(":
            left_to_remove += 1
        elif char == ")":
            if left_to_remove > 0:
                left_to_remove -= 1
            else:
                right_to_remove += 1

    # Step 2: Backtracking function
    def backtrack(index, open_count, close_count, path, left_remain, right_remain):
        if index == len(s):
            if left_remain == 0 and right_remain == 0 and open_count == close_count:
                result.add(path)
            return

        char = s[index]

        if char == "(":
            # Option 1: remove the '('
            if left_remain > 0:
                backtrack(
                    index + 1,
                    open_count,
                    close_count,
                    path,
                    left_remain - 1,
                    right_remain,
                )
            # Option 2: keep the '('
            backtrack(
                index + 1,
                open_count + 1,
                close_count,
                path + char,
                left_remain,
                right_remain,
            )

        elif char == ")":
            # Option 1: remove the ')'
            if right_remain > 0:
                backtrack(
                    index + 1,
                    open_count,
                    close_count,
                    path,
                    left_remain,
                    right_remain - 1,
                )
            # Option 2: keep the ')' if it balances a previous '('
            if close_count < open_count:
                backtrack(
                    index + 1,
                    open_count,
                    close_count + 1,
                    path + char,
                    left_remain,
                    right_remain,
                )

        else:
            # Always include non-parenthesis characters
            backtrack(
                index + 1,
                open_count,
                close_count,
                path + char,
                left_remain,
                right_remain,
            )

    # Step 3: Start backtracking
    backtrack(0, 0, 0, "", left_to_remove, right_to_remove)
    return list(result)
