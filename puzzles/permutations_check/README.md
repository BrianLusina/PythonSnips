# Permutation Game

There are n(n is even) players, conveniently labeled 1,2,3...n. These players will play m rounds of games. In each round
of games. In each round of games, the players are split into 2 teams of n/2 players each. Two players x<y are said to
have played against each other if they were on different teams for one of the m games.

You are given 3 arguments, `n`, `m`, `games`. Your task is to check that for all pairs of players 1<=x, y<=n, player x has
played against y.
games is a 2D list that represents the m rounds of games among n players.

Write a function `check(n, m, games)` that takes in 3 arguments

games is a 2D list with m rows and n columns where `games[i]` is a permutation of `1,2,3...n` representing round
number `i`.
in particular for round `i`,
`games[i][0]`, `games[i][1]`, `games[i][n/2-1]` is on 1 team.
`games[i][n/2]`, `games[i][n/2+1]`, `games[i][n-1]` is on the other team

`check(n, m, games)` should return a boolean. True if and only if all pairs of players have played against each other in
the m rounds of games
