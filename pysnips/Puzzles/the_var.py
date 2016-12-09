print ord("d") - 96
print ord("g") - 96


def the_var(var):
    n = [ord(i) - 96 for i in var.split("+")]
    return sum(n)


print the_var("d+g")
