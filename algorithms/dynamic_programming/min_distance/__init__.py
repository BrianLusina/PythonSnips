from typing import Dict, Tuple


def min_distance(a: str, b: str) -> int:
    """Returns the minimum number of operations required to convert a string a into string b

    Edit distance is a classic DP problem. It is used to quantify the dissimilarity of two given strings by counting
    the minimum possible number of operations required to transform one string into the other.

    Given that the constraints, we assume that a O(m * n) solution would pass.

    Let's define dp[i][j] as the minimum edit distance between the first i character of word1 and the first j characters
     of word2. In example 1, dp[3][2] would be the edit distance between word1[1..3] (HOR) and word2[1..2](RO).

    If the last character is the same, then dp[i][j] would be dp[i - 1][j - 1] because we don't need to perform any
    operation. Otherwise, we need to perform either one. There are three possible ways to do the transformation.

    1. We can transform word1[1..i] to word2[1..j-1] by adding word2[j] afterwards to get word2[1..j].
    2. We can transform word1[1..i-1] to word2[1..j] by deleting word1[i].
    3. We can transform word1[1..i-1] to word2[1..j-1] by exchanging the original word1[i] for word2[j].

    Therefore, the transition would be dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) if word1[i] is
     not equal to word2[j].

    What is the base case then? The base case is simply an edit distance between the empty string and non-empty string,
    i.e. dp[i][0] = i and dp[0][j] = j. The answer would be dp[m][n]. This algorithm is also known as Wagner–Fischer
    algorithm.

    Time Complexity: O(m*n)
    Space Complexity: O(m*n)

    Args:
        a (str): string to convert to string b
        b (str): string to be compared against
    Returns:
        int: minimum number of operations to convert from string a to string b
    """

    # edge cases
    # strings are exactly the same, so no need for performing any operations on it
    if a == b:
        return 0

    # if string a is empty, then it will need the length of string a as the number of operations
    if len(a) == 0:
        return len(b)

    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(m):
        for j in range(n):
            # swap or identical character
            x = dp[i][j] + (0 if a[i] == b[j] else 1)

            # remove last character
            y = dp[i][j + 1] + 1

            # add last character
            z = dp[i + 1][j] + 1

            dp[i + 1][j + 1] = min(x, y, z)

    return dp[m][n]


def min_distance_memoization(word1: str, word2: str) -> int:
    """
    Using similar logic as the above approach but with recursion, and a hash map to cache the values to prevent doing
    repeated work we can achieve the same answer in similar time and space.

    To perform it recursively we must first think of our base cases. That is any empty string, compared to a non-empty
    string. If we use i and j to represent slices of our word as word1[:i] and word2[:j], then all the base cases are
    where either i or j are zero, means we would need to either insert the correct characters to match an empty word1 to
    word2 or delete all the characters of a word1 to match to an empty word2

    Knowing our base cases then, we must figure our what we do after that if we are not in a base case. The first, and
    most obvious one, would be if the current characters of both words match, that is word1[i−1] is equal to word2[j−1],
    then we can just cache the value of that to be what every was the value we receive from our recursive call at
    (i−1,j−1)

    The other option then is when the character doesn't match. In that case, we must either delete, replace, insert a
    character. Meaning we will basically have to perform 1 extra operation than we performed on our calls to (i−1,j),
    (i,j−1) or (i−1,j−1). We should take the one that performed the least amount of operations before to optimize our
     result.

    Remember to cache those results, and we can return our cache result for (i,j) on each iteration to eventually solve
    our problem.

    Time Complexity: O(m∗n), where m is the length of word1 and n is the length of word2. We are going to make m∗n calls
    to our recursive function, reusing work so as not to make more.

    Space Complexity: O(m∗n). Our cache will store m∗n values, to prevent of from having to repeat work we already did.
    """

    # initialize our hash map, cache:
    # key: tuple of values (i, j) where i is our subword word1[:i]
    # and j is the index of our subword word2[:j]
    # value: integer, which represents the number of operations to
    # perform on word1 to create word2.
    cache: Dict[Tuple[int, int], int] = {}

    # our dfs recursive call using parameters i and j as explained
    # above
    def dfs(i: int, j: int) -> int:
        # if we found i and j in the cache, no need to repeat work.
        if (i, j) in cache:
            return cache[(i, j)]
        # base case, if either is 0, then we know we would have
        # to either insert x amount of characters or delete x amount
        # of characters to create our word, x being the number of
        # delete/insert operations we are performing.
        if i == 0 or j == 0:
            return j if j else i
        # if current character match up in each word, then we can
        # reuse work from previous subproblem where the words where
        # the same except for the current character
        if word1[i - 1] == word2[j - 1]:
            # cache the value we get from the recursive call
            cache[(i, j)] = dfs(i - 1, j - 1)
        # character are different, then we need to know the number of
        # operations we used on 3 different subproblems. That is
        # word1[:i - 1] word2[:j]
        # word1[:i]     word2[:j - 1]
        # word1[:i - 1] word2[:j - 1]
        else:
            op1 = dfs(i - 1, j)
            op2 = dfs(i, j - 1)
            op3 = dfs(i - 1, j - 1)
            # cache the results of those subproblems, and make sure
            # to add 1 to the smallest of those 3 subproblems. We
            # want the least number of operations, so we take the
            # the min value.
            cache[(i, j)] = 1 + min(op1, op2, op3)
        # return our results for subproblem at (i, j)
        return cache[(i, j)]

    # Call our recursive function, and return the answer.
    return dfs(len(word1), len(word2))
