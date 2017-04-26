class ConsecutiveString(object):
    def __init__(self, starr, k):
        self.starr = starr
        self.k = k

    def longest_consec(self):
        result = ""

        if 0 < self.k <= len(self.starr):
            for index in range(len(self.starr) - self.k + 1):
                s = ''.join(self.starr[index:index + self.k])
                if len(s) > len(result):
                    result = s

        return result


def longest_consec(starr, k):
    result = ""
    if 0 < k <= len(starr):
        for index in range(len(starr) - k + 1):
            s = ''.join(starr[index:index + k])
            if len(s) > len(result):
                result = s

    return result
