def uni_total(string):
    return sum([ord(i) for i in string])


print uni_total("a")  # 97)
print uni_total("b")  # 98)
print uni_total("c")  # 99)
print uni_total("")  # 0)
print uni_total("aaa")  # , 291)
print uni_total("abc")  # 294)
print uni_total("Mary Had A Little Lamb")  # ,1873)
print uni_total("Mary had a little lamb")  # ,2001)
print uni_total("CodeWars rocks")  # 1370)
print uni_total("And so does Strive")  # ,1661)