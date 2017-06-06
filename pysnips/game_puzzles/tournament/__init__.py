def tally(results):
    """
    draws a table from given results and ranks the team by points
    :param results: tuple of results for tournament
    :return: formatted table of results with teams ranked by points
    :rtype: tuple
    """
    output = ['Team                           | MP |  W |  D |  L |  P']
    # perform sanity check on results
    # if results is empty, return the header alone
    if results == "":
        return "".join(output)
    outcomes = results.split("\n")
    for outcome in outcomes:
        team1, team2, match_result = outcome.split(";")

