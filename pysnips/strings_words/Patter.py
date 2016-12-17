def pattern(n):
    return '\n'.join(['1'] + ['1' + '*' * (i - 1) + str(i) for i in xrange(2, n + 1)])


print("Testing for pattern(n) function")
print("Actual:", pattern(3), "Expected:", "1\n1*2\n1**3")
print("Actual:", pattern(7), "Expected:", "1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7")
print("Actual:", pattern(20),
      "Expected:" "1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7\n1*******8\n1********9\n1*********10\n1**********11"
      "\n1***********12\n1************13\n1*************14\n1**************15\n1***************16\n1****************17"
      "\n1*****************18\n1******************19\n1*******************20")
