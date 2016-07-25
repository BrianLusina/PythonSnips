print("Welcome to Interact.")

# obtain user input
user_name = input("First, we need a name! What is your name?")

# store user answer in variable
user_answer = input("Welcome, " + user_name + "! Do you like food?")

# start conditionals
if user_answer == "yes" or "YES" or "y" or "Yes" or "Y":
    print("Of course you do, you're human")
    user_answer2 = input("What is your favorite food?")
    user_answer3 = input("Nice!" + user_answer2 + "! Do you like Guacamole?")
    if user_answer3 == "yes" or "YES" or "y" or "Yes" or "Y":
        print("Awesome!")
    else:
        print("But WHY!! You must give it a chance")

elif user_answer == "NO" or "no" or "n" or "N":
    user_answer3 = input("What?! Why?")
    print("You know what, never mind. You have your reasons. I shall respect that")