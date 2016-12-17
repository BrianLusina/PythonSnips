# -*- coding: utf-8 -*-
from itertools import groupby
import re


def encode(stringtoencode):
    return "".join(['{}{}'.format(len(list(g)), k) for k, g in groupby(stringtoencode)])


def decode(strintodecode):
    return re.sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), strintodecode)

