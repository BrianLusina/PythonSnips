from typing import Iterator, Optional
from itertools import groupby
from re import sub


def encode_2(text: str):
    return "".join([f"{len(list(g))}{k}" for k, g in groupby(text)])


def decode_2(text: str):
    return sub(r"(\d+)(\D)", lambda m: m.group(2) * int(m.group(1)), text)


def decode(text: str):
    return sub(r"(\d+)(\D)", lambda m: m.group(2) * int(m.group(1)), text)


def encode(text: str, limit: Optional[int] = None):
    def single_helper(key: str, group: Iterator[str]) -> str:
        group_len = len(list(group))
        if limit:
            cap = limit - 1
            if group_len >= limit:
                # split this into parts that sum up to limit, so, if it is 13, we need it to be 9 and 4
                rem = group_len % cap
                return f"{cap}{key}{rem}{key}"
        return key if group_len == 1 else str(group_len) + key

    return "".join(single_helper(key, group) for key, group in groupby(text))
