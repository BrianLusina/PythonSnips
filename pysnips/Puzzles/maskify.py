import re


def maskify(cc):
    return cc if len(cc) <= 4 else re.sub(r'.', r'#', cc[:-4]) + cc[len(cc) - 4:]


print "Actual:", maskify("4556364607935616"), "Expected:", "############5616", maskify(
    "4556364607935616") == "############5616"
print maskify("64607935616") == "#######5616"
print maskify("1") == "1"
print maskify("") == ""
print maskify("Skippy") == "##ippy"
print maskify("Nananananananananananananananana Batman!") == "####################################man!"
print maskify("123")
