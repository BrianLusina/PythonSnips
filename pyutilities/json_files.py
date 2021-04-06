import json
from pprint import pprint

# store the json file in a variable
json_data = open("User_Data.json")

# enter the file, load it into a variable and close the file
with json_data as data_file:
    data = json.load(data_file)


class UserData(object):
    """
    Class to check the JSON file of user data,
    check if user id is an integer
    Store the json file in a variable and loop through
        use with filename as variable to load the json data and store in a variable
    use this loaded data to loop through checking for user data
    if the input is an integer, obtain user id
    loop through each line
    """

    @staticmethod
    def obtain_id():
        uid = input("Enter User ID: ")

        if isinstance(int(uid), int):
            user_id = int(uid)
            # pprint(data)
            for x in data:
                if x.get('id') == user_id:
                    print("---" * 10 + "\n" +
                          "User Found...\n" +
                          "---" * 10 + "\n" +
                          "ID: " + str(x.get('id')) + "\n" +
                          "First Name: " + x.get('first_name') + "\n" +
                          "Last Name: " + x.get("last_name") + "\n" +
                          "Gender: " + x.get('gender') + "\n" +
                          "Email: " + x.get('email') + "\n" +
                          "---" * 10
                          )
        else:
            print("Please enter a valid id")

    """
     Class to check stats of the JSON file, check the count for genders
     Returns the count for male, female in a list, with each list containing data for each gender, e.g
     [[Males: 46],[Females:54]]
     """

    @staticmethod
    def stats():
        male_count, female_count = 0, 0

        for x in data:
            if x.get('gender') == "Male":
                male_count += 1
            elif x.get('gender') == "Female":
                female_count += 1
        print([["Males", male_count], ["Females", female_count]])

    """
    Problem description: Sort through a JSON file, checking for the first name
    store the first names in a list
    sort the list of first names
    for each name in the sorted data, loop through each dictionary obtaining first names, store in a list
    find the rest of the data
    """

    @staticmethod
    def data_sorter():
        sorted_data = []
        firsts = [user.get('first_name') for user in data]

        user_request = input("Reverse Data?(y/n)")
        if user_request == "y" or user_request == "Y":
            sort_names = sorted(firsts, reverse=True)
            for name in sort_names:
                for user in data:
                    if user.get("first_name") == name:
                        sorted_data.append(user)
            return sorted_data
        else:
            sort_names = sorted(firsts)
            for name in sort_names:
                for user in data:
                    if user.get("first_name") == name:
                        sorted_data.append(user)

            return sorted_data


UserData.obtain_id()
UserData.stats()
pprint(UserData.data_sorter())
