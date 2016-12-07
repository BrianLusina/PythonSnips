print("Welcome to Interact.")

# obtain user input
user_name = input("First, we need a name! What is your name?")

# store user answer in variable
user_answer = input("Welcome, " + user_name + "! Do you like food?")

# start conditionals
if user_answer == "yes" or user_answer == "YES" or user_answer == "y" or user_answer == "Yes" or user_answer == "Y":
    print("Of course you do, you're human")
    user_answer2 = input("What is your favorite food?")
    user_answer3 = input("Nice!" + user_answer2 + "! Do you like Guacamole?")
    if user_answer3 == "yes" or user_answer3 == "YES" or user_answer3 == "y" or user_answer3 == "Yes" or user_answer3 == "Y":
        print("Awesome!")
    elif user_answer3 == "no" or user_answer3 == "n" or user_answer3 == "No" or user_answer3 == "N" or user_answer3 == "NO":
        print("But WHY!! You must give it a chance")

elif user_answer == "NO" or user_answer == "no" or user_answer == "n" or user_answer == "N" or user_answer == "No":
    user_answer3 = input("What?! Why?")
    print("You know what, never mind. You have your reasons. I shall respect that")

else:
    print("I did'nt quite get that, do repeat please")
