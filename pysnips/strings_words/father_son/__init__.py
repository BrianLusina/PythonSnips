def sc(s):
    ret = []
    for c in s:
        if c.isupper():
            if chr(ord(c) + 32) in s:
                ret.append(c)
        elif c.islower():
            if chr(ord(c) - 32) in s:
                ret.append(c)
    return ''.join(ret)
