"""
Small entertainment in flight program for recommending movies to people to watch while they are in flight
should return a boolean indicating whether there are 2 movies to watch whose lengths sum up to the flight 
length or are less than the flight length
"""


def in_flight_entertainment(flight_length, movie_lengths):
    """
    Loops through the movie lengths and checks whether there are 2 movies to watch which sum up to the flight
    length
    :param flight_length: length of the flight in minutes 
    :param movie_lengths: list of movie lengths
    :return: 2 recommended movies to watch that are equal to or less than the flight length
    :rtype: bool
    """
    # will hold reference to the movies already summed and checked to prevent duplication
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length

        # if there is a 2nd matching movie length we have seen already we short circuit early
        if matching_second_movie_length in movie_lengths_seen:
            return True

        movie_lengths_seen.add(first_movie_length)

    # we never found a match
    return False
