def narcissistic(value):
    l = len(str(value))  # length of number
    return sum([pow(int(i), l) for i in str(value)]) == value


print "Testing for narcissistic(v) function"
print (narcissistic(7) == True)  # '7 is narcissistic');
print(narcissistic(371) == True)  # '371 is narcissistic');
print(narcissistic(122) == False)  # '122 is not narcissistic')
print(narcissistic(4887) == False)  # '4887 is not narcissistic')
