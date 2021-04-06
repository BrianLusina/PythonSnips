def num_trees(n: int) -> int:
    """
    For all possible values of i, consider i as root, then [1….i-1] numbers will fall in the left subtree and [i+1….n] numbers will fall in the right subtree. 
    So, add (i-1)*(n-i) to the answer. 
    The summation of the products will be the answer to the number of unique BST.    
    """
    dp = [0] * (n + 1)

    dp[0], dp[1] = 1, 1

    for x in range(2, n + 1):
        for y in range(1, x + 1):
            dp[x] = dp[x] + (dp[x - y] * dp[y - 1])

    return dp[n]
