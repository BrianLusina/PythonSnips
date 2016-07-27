"""
Name, email, phone number
"""

user_name = input("Hello! What is your name?")


def user_file():
    # check if user name is in file
    # create a file instance,
    file = open("user.txt", "r+")

    if user_name not in file.readlines():
        file.write(user_name)
        file.close()
        return "Success " + user_name + " written to file"
    else:
        return "Error,"+ user_name + " exists"

