import json
from pprint import pprint

# store the json file in a variable
json_data = open("User_Data.json", "r")

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
    Problem description: Sort through a JSON file, checking for the first name
    store the first names in a list
    sort the list of first names
    for each name in the sorted data, find the rest of the data
    """
    @staticmethod
    def data_sorter():
        firsts = []
        sorted_data = []
        for user in data:
            firsts.append(user.get('first_name'))

        sort_names = sorted(firsts)
        for name in sort_names:
            for user in data:
                if user.get("first_name") == name:
                    sorted_data.append(user)

        return sorted_data

# UserData.obtain_id()
print(UserData.data_sorter())
