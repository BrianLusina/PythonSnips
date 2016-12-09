from ModulesDemo import tribonacciModule

print("Welcome to Tribonacci!\nToday we shall get a tribonacci sequence. We will need a limit from you.\n")
user_input = int(input("Your number for today? "))
print(tribonacciModule.tribonacci(int(user_input)))
