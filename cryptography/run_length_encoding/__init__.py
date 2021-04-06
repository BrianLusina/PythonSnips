# -*- coding: utf-8 -*-
from itertools import groupby
from re import sub


def encode_2(encode_str):
    return "".join(['{}{}'.format(len(list(g)), k) for k, g in groupby(encode_str)])


def decode_2(decode_str):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), decode_str)


def decode(string):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), string)


def encode(string):
    def single_helper(k, g):
        l = len(list(g))
        return k if l == 1 else str(l) + k

    return ''.join(single_helper(key, group) for key, group in groupby(string))
