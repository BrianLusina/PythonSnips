class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        """
        Gets the latest score
        :return: latest score
        :rtype: int
        """
        return self.scores[-1]

    def personal_best(self):
        """
        Returns the best score in the list
        :return: Maximum score in the list
        :rtype: int
        """
        return max(self.scores)

    def personal_top(self):
        """
        Sorts the scores in descending order from left to right and returns the
        top 3 highest scores
        :return: list of values sorted in descending order
        :rtype: list
        """
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        latest_score = self.latest()
        maximum_score = self.personal_best()
        message = f"Your latest score was {latest_score}."
        message_end = f"your personal best!"

        if latest_score == maximum_score:
            return f"{message} That's {message_end}"
        elif latest_score < maximum_score:
            diff = maximum_score - latest_score
            return f"{message} That's {diff} short of {message_end}"
