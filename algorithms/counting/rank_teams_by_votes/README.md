# Rank Teams by Votes

In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first 
position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the
ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically
based on their team letter.

You are given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according
to the ranking system described above.

Return a string of all teams sorted by the ranking system.

## Examples

Example 1:
```text
Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: 
Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
Team B was ranked second by 2 voters and ranked third by 3 voters.
Team C was ranked second by 3 voters and ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team, and team B is the third.
```

Example 2:
```text
Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation:
X is the winner due to the tie-breaking rule. X has the same votes as W for the first position, but X has one vote in
the second position, while W does not have any votes in the second position. 
```

Example 3:

```text
Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter, so their votes are used for the ranking.
```

## Constraints

- 1 <= votes.length <= 1000
- 1 <= votes[i].length <= 26
- votes[i].length == votes[j].length for 0 <= i, j < votes.length.
- votes[i][j] is an English uppercase letter.
- All characters of votes[i] are unique.
- All the characters that occur in votes[0] also occur in votes[j] where 1 <= j < votes.length.

## Hints

- Build array rank where rank[i][j] is the number of votes for team i to be the j-th rank.
- Sort the teams by rank array. if rank array is the same for two or more teams, sort them by the ID in ascending order.

## Topics

- Array
- Hash Table
- String
- Sorting
- Counting

## Solution

The key intuition for solving this problem is to efficiently keep track of the vote counts each team receives for each
position. We create a 2D array for this purpose, where the rows represent the teams and the columns represent the vote
counts for each position. For each team in `votes[i][j]`, we update its vote count at the jth index in the counts array.
After processing all votes, we sort the counts array based on the values in each row, prioritizing the row with the
lowest value at the first index. If there is a tie, the row with the lowest value at the second index takes precedence,
and so on. The final result is constructed using team's name corresponding to each row in the sorted array.

Using the above intuition, the solution can be implemented as follows:

1. Create a 2D array counts with dimensions 26×27 to store vote counts for each team.
   - The first dimension (26) corresponds to the teams (A–Z), as there can be a maximum of 26 teams.
   - The second dimension (27) holds the vote counts for each rank. Because there can be a maximum of 26 teams, the
     maximum rank a team can get is 26 . It includes an additional column to store the team’s name to ensure that we
     don’t lose track of which team’s data is in each row after sorting.
2. For each team index t, store the team’s name at counts[t][26]. This keeps track of which team corresponds to each row
   in the counts array.
3. Start iterating through each string votes[i] to process the ranking given by each voter.
4. For each character `votes[i][j]` representing a team in the vote, decrement its rank in the counts. This is because each
   row in counts denotes the rank of a team; a lower count indicates a higher rank.
5. Sort the counts array based on the values in each row. The sorting is done such that the row with the lowest value at
   the first index comes first. If there is a tie, the row with the lowest value at the second index takes precedence,
   and so on.
6. Construct the final result by retrieving the team name stored at the last index (counts[i][26]) in the sorted counts.
7. Return the constructed result, which contains all teams sorted according to the specified ranking system.

### Time Complexity

Given the length of the votes is n, the time complexity can be calculates as:

- The time complexity of iterating each character in each string in votes is O(n×26), which is simplified to O(n).
- The time complexity of sorting counts is `O(26×26log(26))`, which is simplified to O(1)
- The time complexity of building the result string is O(26), which is simplified to O(1).

Therefore, the time complexity of the above algorithm is O(n).

### Space Complexity

The algorithm’s space complexity is O(26×27) occupied by counts, which is simplified to O(1).
