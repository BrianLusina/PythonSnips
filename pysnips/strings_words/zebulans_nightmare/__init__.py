def zebulans_nightmare(functionName):
    # replace the underscore with a space to create separate words and split them into a list
    fn = functionName.replace("_", " ").split()
    f_let = ""
    # add first element to a new list
    out = [fn[0]]
    # take only the 2nd and consecutive elements
    for i in fn[1:]:
        # capitalize the first letter only of each word
        f_let = i.title()
        # add each new word to the list
        out.append(f_let)
    # return this new list
    return "".join(out)


print(zebulans_nightmare("goto_next_kata"))
