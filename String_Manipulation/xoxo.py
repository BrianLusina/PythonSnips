def Xoxo(string):
    string = string.lower()
    if string.find("x") != -1 or string.find("o") != -1:
        return string.count("x") == string.count("o")
    else:
        return False

# keep the function call
print(Xoxo("have fun..xoxo"))
print(Xoxo("6546516541465"))