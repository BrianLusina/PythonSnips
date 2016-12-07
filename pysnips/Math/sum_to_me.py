def summation(x):
    return sum(range(1, x + 1)) if isinstance(x, int) else "Error 404"


print("Actual:", summation(10), "Expected:", 55, summation(10) == 55)
print(summation(5) == 15)
print(summation("538") == "Error 404")
print(summation(67.9) == "Error 404")
