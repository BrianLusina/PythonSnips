def append_characters(source: str, target: str) -> int:
    if source == target:
        return 0

    target_len = len(target)
    ptr_target = 0

    for char in source:
        if ptr_target >= target_len:
            break

        target_char = target[ptr_target]
        if char == target_char:
            ptr_target += 1

    return target_len - ptr_target


def append_characters_2(source, target):
    source_index = 0  # current position in source
    target_index = 0  # next character index to match in target
    source_length = len(source)
    target_length = len(target)

    # Walk through source and try to match target in order
    while source_index < source_length and target_index < target_length:
        if source[source_index] == target[target_index]:
            target_index += (
                1  # matched target[target_index], move to the next needed char
            )
        source_index += 1  # always advance in source

    # target_length - target_index is exactly how many characters remain unmatched in target
    # and therefore must be appended to source.
    return target_length - target_index
