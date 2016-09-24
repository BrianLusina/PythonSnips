def is_valid_HK_phone_number(number):
    #check if a space is at the end or at the beginning
    if number.startswith(" ") or number.endswith(" "):
        return False
    #if there are spaces in the middle or none at all
    elif number.count(" ") == 2 or number.count(" ") == 0:
        return False
    #check for validity of numbers
    else:
        nList = number.split()
        if nList[0].isdigit() and len(nList[0]) == 4:
            return True
        elif nList[1].isdigit() and len(nList[1]) == 4:
            return True
        else:
            return False

def has_valid_HK_phone_number(number):

    return filter(lambda x:x.isdigit(),number)

print ("Testing for is_valid_HK_phone_number method")
print is_valid_HK_phone_number("1234 5678") # True passed
print is_valid_HK_phone_number("2359 1478") #True passed
print is_valid_HK_phone_number("85748475")  #False passed
print is_valid_HK_phone_number("3857  4756") #False passed
print is_valid_HK_phone_number("sklfjsdklfjsf") #False passed
print is_valid_HK_phone_number("     1234 5678   ") #False passed
print is_valid_HK_phone_number("123456789") #False passed
print is_valid_HK_phone_number(" 987 634 ") #False passed
print is_valid_HK_phone_number("    6    ") #False passed
print is_valid_HK_phone_number("9684 2396") #True passed
print is_valid_HK_phone_number("0000 0000") #True passed
print is_valid_HK_phone_number("abcd efgh") #False passed
print is_valid_HK_phone_number("836g 2986") #False passed
print is_valid_HK_phone_number("8A65 2986") #False passed
print is_valid_HK_phone_number("8c65 2i86") #False passed
print is_valid_HK_phone_number("8368 2aE6") #False passed
print is_valid_HK_phone_number("83680 28968") #False passed
print(has_valid_HK_phone_number("Hello, my phone number is 1234 5678")) #True
print(has_valid_HK_phone_number("I wonder if 2359 1478 is a valid phone number?")) #True
print(has_valid_HK_phone_number("85748475 is definitely invalid"))#False
print(has_valid_HK_phone_number("'3857  4756' is so close to a valid phone number!"))#False
print(has_valid_HK_phone_number("sklfjsdklfjsf"))# False
print(has_valid_HK_phone_number("     1234 5678   ")) # True
print(has_valid_HK_phone_number("What about abcd efgh?"))#False
print(has_valid_HK_phone_number("What about 9684 2396?")) #True)
print(has_valid_HK_phone_number("And 836g 2986?")) #False)
print(has_valid_HK_phone_number("skldfjsdklfjs0000 0000skldfjslkdfjs"))#True)
print(has_valid_HK_phone_number("123456789 is invalid")) #False
print(has_valid_HK_phone_number("sdfssdfsdfdf 987 634 sdfsddsds"))#False
print(has_valid_HK_phone_number("\n\n    6    \n\n")) #False
print(has_valid_HK_phone_number("sdfsdsdfdf8A65 2986sdfsddfs"))#False
print(has_valid_HK_phone_number("iwoeurwoeuwo8368 2aE6"))#False
print(has_valid_HK_phone_number("8c65 2i86wioeruwioeruweoi"))#False
