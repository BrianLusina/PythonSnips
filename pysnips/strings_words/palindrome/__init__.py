def is_palindrome(a):
    return str(a) == str(a)[::-1]


def longest_palindrome(s):
    s, final_str = s.lower(), ""
    if s == "":
        return 0
    else:
        for y, item in enumerate(s):
            for x, item in enumerate(s):
                tr = s[y:x + 1]
                if is_palindrome(tr) and (len(tr) > len(final_str)):
                    final_str = tr

    return len(final_str)
