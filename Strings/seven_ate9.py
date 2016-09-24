import re


def seven_ate9(sevens):
    return re.sub(r"7+9(?=7)", "7", sevens)


print "Actual: " + seven_ate9('165561786121789797'), "Expected: " + '16556178612178977', seven_ate9(
    '165561786121789797') == '16556178612178977'
print "Actual: " + seven_ate9('797'), "Expected: " + "77", seven_ate9('797') == "77"
print "Actual: " + seven_ate9('7979797'), "Expected: " + "7777", seven_ate9('7979797') == '7777'
