import random
import string


class Password(object):
    """
    static method will perform the random password generator
    get a random choice from the ascii letters and digits and symbols for range between 1-10
    join the string to get one full password
    validate_scale: function to check if the user scale is an integer and is in range 1-10
    """
    def __init__(self, scale):
        self.scale = scale

    def generate_pass(self):
        return "New Password: " + ''.join(random.choice(string.ascii_letters + string.digits + ".',={}[]-/|\£$%^&*()_+~#@?><") for _ in range(self.scale))

    @staticmethod
    def validate_scale(n):
        return isinstance(n, int) and range(1, 11)


def user_request():
    # request user pass and store user response
    hard_pass_opt = input("How strong a password do you want? Scale from 1-10 ")
    hard_pass_opt = int(hard_pass_opt)
    # call generate pass
    if Password.validate_scale(hard_pass_opt):
        try:
            new_password = Password(hard_pass_opt)
            return new_password.generate_pass()
        except TypeError:
            return "Oh Shacks! Error. Please Try again."
    else:
        return "Please enter a valid number for your scale."


# decorator function to format password generator
def pass_decorator(func):
    def wrap_pass():
        func()
        print("*-" * 5 + "\nThank you."+"\n-*"*5)
    return wrap_pass()


@pass_decorator
def print_pass():
    print(user_request())
