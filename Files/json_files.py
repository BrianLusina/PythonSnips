import json
from pprint import pprint

uid = input("Enter User ID: ")


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
        json_data = open("User_Data.json", "r")
        with json_data as data_file:
            data = json.load(data_file)

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


UserData.obtain_id()
