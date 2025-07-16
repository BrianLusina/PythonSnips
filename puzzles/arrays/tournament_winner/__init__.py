from typing import List, Dict


def tournament_winner(competitions: List[List[str]], results: List[int]) -> str:
    # We need to store a dictionary with the name of the team as the key and the number of points as the value
    # 3 points for a win, 0 points for a loss
    winner = ""
    teams: Dict[str, int] = {}
    for competition, result in zip(competitions, results):
        # result of 0 means that the away team won
        # add the teams to the dictionary with the number of points
        home_team = competition[0]
        away_team = competition[1]

        teams[home_team] = teams.get(home_team, 0)
        teams[away_team] = teams.get(away_team, 0)

        if result == 0:
            teams[away_team] = teams.get(away_team, 0) + 3
        else:
            teams[home_team] = teams.get(home_team, 0) + 3

    # find the team with the most points
    for team, points in teams.items():
        if points > teams.get(winner, 0):
            winner = team

    return winner
