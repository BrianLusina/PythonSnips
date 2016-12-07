from collections import Counter
import string

def sc(s):
    ret=[]
    for c in s:
        if c.isupper():
            if chr(ord(c)+32) in s:
                ret.append(c)
        elif c.islower():
            if chr(ord(c)-32) in s:
                ret.append(c)
    return ''.join(ret)

print(sc("Aab"), "Aa")
print(sc("AabBc"), "AabB")
print(sc("SONson"), "SONson")
print(sc("FfAaTtHhEeRr"), "FfAaTtHhEeRr")
print(sc("SONsonfather"), "SONson")
print(sc("sonfather"), "")
print(sc("DONKEYmonkey"), "ONKEYonkey")
print(sc("monkeyDONKEY"), "onkeyONKEY")
print(sc("BANAna"), "ANAna")
