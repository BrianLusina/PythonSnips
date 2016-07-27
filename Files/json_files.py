# create the data.json file
json = open("data.json", "w")

user_data = input("Please enter your age")

json.write(user_data)
json.close()