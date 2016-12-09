user_name = input("Hello! What is your name?")


class UserDatabase(object):
    @staticmethod
    def user_db():
        # check if user name is in file
        # create a file instance,
        file = open("user.txt", "r+")

        if user_name not in file.readlines():
            file.write(user_name + "\n")
            file.close()
            print("success")
            return "Success " + user_name + " written to file"
        else:
            print("Error")
            return "Error," + user_name + " exists"


UserDatabase.user_db()
