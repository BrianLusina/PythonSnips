import unittest

from pystrings.balanced_paren import balanced_parens


class BalancedParensTestCase(unittest.TestCase):
    def sample_tests(self):
        for n, exp in [[0, [""]],
                       [1, ["()"]],
                       [2, ["(())", "()()"]],
                       [3, ["((()))", "(()())", "(())()", "()(())", "()()()"]]]:
            actual = balanced_parens(n)
            actual.sort()
            self.assertEqual(actual, exp)

    def random_tests(self):
        def ref_sol(n):
            return list(dfs([], 0, 0, n))

        def dfs(s, open_count, close_count, max_p):
            if close_count == max_p:
                yield "".join(s)
                return
            if open_count > close_count:
                s.append(')')
                yield from dfs(s, open_count, close_count + 1, max_p)
                s.pop()
            if open_count < max_p:
                s.append('(')
                yield from dfs(s, open_count + 1, close_count, max_p)
                s.pop()

        from random import shuffle

        rng = list(range(13))
        shuffle(rng)
        for n in rng:
            exp = ref_sol(n)
            act = balanced_parens(n)
            exp.sort()
            act.sort()
            if len(exp) > 1000:
                self.assertEqual(exp == act, 'Nope...(n={})'.format(n))
            else:
                self.assertEqual(act, exp)


if __name__ == '__main__':
    unittest.main()
