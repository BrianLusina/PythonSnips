def the_var(var):
    n = [ord(i) - 96 for i in var.split("+")]
    return sum(n)
