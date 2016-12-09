def to_jaden_case(string):
    return " ".join([word[0].upper() + word[1:] for word in string.split()])

quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
