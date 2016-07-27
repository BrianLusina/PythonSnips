import json


class JSON_Stats(object):
    """
    Class to check stats of the JSON file, check the count for genders
    Returns the count for male, female in a list, with each list containing data for each gender, e.g
    [[Males: 46],[Females:54]]
    """
    @staticmethod
    def stats():
        json_data = open("User_Data.json", "r")
        male_count, female_count = 0, 0
        with json_data as data_file:
            data = json.load(data_file)

        for x in data:
            if x.get('gender') == "Male":
                male_count += 1
            elif x.get('gender') == "Female":
                female_count += 1
        print([["Males", male_count], ["Females", female_count]])

JSON_Stats.stats()
