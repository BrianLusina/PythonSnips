class UserDatabase(object):
    @staticmethod
    def user_db():
        # check if user name is in file
        # create a file instance,
        file = open("user.txt", "r+")

        if user_name not in file.readlines():
            file.write(user_name)
            file.close()
            return "Success " + user_name + " written to file"
        else:
            return "Error," + user_name + " exists"

"""
Name, email, phone number
"""

user_name = input("Hello! What is your name?")

# check if user name is in file
# create a file instance,
file = open("user.txt", "r+")

# check is user name is not in file
if user_name not in file.readlines():
    # if not, write to it
    file.write(user_name + "\n")
    # close it to enable data to reach target file
    file.close()
    print("Success " + user_name + " written to file")
else:
    # return an error message
    print("Error," + user_name + " exists")
    file.close()