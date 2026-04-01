from typing import DefaultDict, List
from collections import defaultdict


def rank_teams_using_hash_map(votes: List[str]) -> str:
    """
    Ranks teams given a list of votes.
    Args:
        votes (List[str]): List of votes.
    Returns:
        str: Correctly ranked teams.
    """
    if not votes:
        return ""
    if len(votes) == 1:
        return votes[0]

    # each team's number of votes is equal
    votes_per_team = len(votes[0])
    # stores a mapping of the team's name to the number of votes per position
    # so, e.g. {'A': [5, 0, 0], 'B': [0, 2, 3], ...}, indicates that A received 5 votes for position 1
    # and B received 2 votes for position 2 and 3 for position 3, etc.
    teams: DefaultDict[str, List[int]] = defaultdict(list)

    # Iterate through the votes. Getting the position each voter ranked the given team
    for voter in votes:
        # For each voter, get where they ranked the given team
        for position, team in enumerate(voter):
            # If the team already exists in the mapping
            if team in teams:
                teams[team][position] += 1
            else:
                # the team has not yet been captured, so, we set the count of votes per team
                teams[team] = [0] * votes_per_team
                teams[team][position] = 1

    sorted_teams = sorted(
        teams.items(), key=lambda item: ([-x for x in item[1]], item[0])
    )

    return "".join(t[0] for t in sorted_teams)


def rank_teams_counting(votes: List[str]) -> str:
    counts: List[List[int | str]] = [[0] * 27 for _ in range(26)]

    for t in range(26):
        counts[t][26] = chr(ord("A") + t)

    for i in range(len(votes)):
        for j, c in enumerate(votes[i]):
            counts[ord(c) - ord("A")][j] -= 1

    counts.sort()

    res = ""

    for i in range(len(votes[0])):
        res += counts[i][26]

    return res
