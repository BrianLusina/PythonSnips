import re
line = "===================================================================="
print("Raw strings are used to avoid strings from escaping")
expression = r"expression" #raw string with the pattern expression
sent = r"I dont't know about you, but I want a burger. Do you want a burger?"
pat = r"spam"

print re.match(expression,"expression") #returns an object if true
print re.search("I",sent) #returns an object if true,None otherwise
print re.findall("burger",sent) #prints ["burger","burger"]
print re.finditer("burger",sent) #returns an iterator, an object

pam = r"pam"
match = re.search(pam, "eggspamsausage")
if match:
   print(match.group()) #returns pam
   print(match.start()) #returns 4
   print(match.end())   #returns 7
   print(match.span()) #returns (4,7)

intro ="My name is Brian, I shall soon conquer this sad blue rock called Earth"
print re.sub("Brian","Lusina The Great",intro) #to replace Brian in intro with Lusina The Great

#Metacharacters
print("This shall display use of metacharacters")
write = r"wr.te"
if re.match(write,"write"):
    print "Match found for write"
elif re.match(write,"wrote"):
    print "Match found for wrote!"

sting = r"sting$"
if re.match(sting,"stings"):
    print "Match found for sting"

print(line)
print("Character classes provide a way to match only one of a specific set oc characters")
vowels,qwerty = r"[aeiou]","qwerty"
alphabet,alpha8 = r"[A-Za-z][0-9]","AlPha8"
phraseInvert,phrase=r"[^A-Z]","This may print"
eggsBacon,eggsBaconPhrase = r"egg(bacon)*","eggs and bacons are awesome!"
eggMatch = re.match(eggsBacon,eggsBaconPhrase)
vowelMatch= re.search(vowels,qwerty)
alphabetMatch = re.search(alphabet,alpha8)
alphaInvertMatch = re.search(phraseInvert, phrase)

if vowelMatch:
    print "Match found for " + vowelMatch.group() +" in "+ qwerty

if alphabetMatch:
    print "Match found for " + alphabetMatch.group() + " in " + alpha8

if alphaInvertMatch:
    print "Match found! First match is " + alphaInvertMatch.group()+ " in " + phrase

if eggMatch:
    print "Match found. First match is " + eggMatch.group() + " in "+ eggsBaconPhrase


"""
Your task is to define a function gymSlang which accepts a string argument and does the following:

Replace all instances of "probably" to "prolly"
Replace all instances of "i am" to "i'm"
Replace all instances of "instagram" to "insta"
Replace all instances of "do not" to "don't"
Replace all instances of "going to" to "gonna"
Replace all instances of "combination" to "combo"
Your replacement regexes should be case-sensitive, only replacing the words above with slang if the detected pattern is in lowercase. However, please note that apart from 100% lowercase matches, you will also have to replace matches that are correctly capitalized (e.g. "Probably" => "Prolly" or "Instagram" => "Insta").

Finally, your code will be tested to make sure that you have used RegExp replace in your code.
"""
replacements = ("probably", "prolly"), ("Probably", "Prolly"), ("i am", "i'm"), ("I am", "I'm"), (
"instagram", "insta"), ("Instagram", "Insta"), ("do not", "don't"), ("Do not", "Don't"), ("going to", "gonna"), (
               "Going to", "Gonna"), ("combination", "combo"), ("Combination", "Combo")
def gym_slang(phrase):
    phrase = re.sub(r'([pP])robably', r'\1rolly', phrase)
    phrase = re.sub(r'([iI]) am', r"\1'm", phrase)
    phrase = re.sub(r'([iI])nstagram', r'\1nsta', phrase)
    phrase = re.sub(r'([dD])o not', r"\1on't", phrase)
    phrase = re.sub(r'([gG])oing to', r'\1onna', phrase)
    phrase = re.sub(r'([cC])ombination', r'\1ombo', phrase)

    return phrase

print line
print gym_slang("When I miss few days of gym") # "When I miss few days of gym")
print gym_slang("Squad probably think I am fake") #"Squad prolly think I'm fake")
print gym_slang("Whole squad probably bigger than me now") # "Whole squad prolly bigger than me now")
print gym_slang("No selfie to post on Instagram either") #"No selfie to post on Insta either")
print gym_slang("Gym crush probably found someone else"), #"Gym crush prolly found someone else")
print gym_slang("What if I die fat"),#"What if I die fat")
print gym_slang("What if I do not fit in my clothes now")# "What if I don't fit in my clothes now")
print gym_slang("Going to feel like a new gym member")# "Gonna feel like a new gym member")
print gym_slang("wait what was my lock combination")# "wait what was my lock combo")
print gym_slang("that skinny hoe can probably outlift me now")# "that skinny hoe can prolly outlift me now")
print gym_slang("probably Probably")# "prolly Prolly")
print gym_slang("i am I am")# "i'm I'm")
print gym_slang("instagram Instagram")# "insta Insta")
print gym_slang("do not Do not")# "don't Don't")
print gym_slang("going to Going to")# "gonna Gonna")
print gym_slang("combination Combination")# "combo Combo")
print gym_slang("probably Probably probably Probably probably Probably probably Probably probably Probably")# "prolly Prolly prolly Prolly prolly Prolly prolly Prolly prolly Prolly")
print gym_slang("i am I am i am I am i am I am i am I am i am I am i am I am")# "i'm I'm i'm I'm i'm I'm i'm I'm i'm I'm i'm I'm")
print gym_slang("instagram Instagram instagram Instagram instagram Instagram instagram Instagram instagram Instagram")# "insta Insta insta Insta insta Insta insta Insta insta Insta")
print gym_slang("do not Do not do not Do not do not Do not do not Do not")# "don't Don't don't Don't don't Don't don't Don't")
print gym_slang("Going to going to Going to Going to going to Going to Going to going to Going to")# "Gonna gonna Gonna Gonna gonna Gonna Gonna gonna Gonna")
print gym_slang("combination combination Combination combination Combination")# "combo combo Combo combo Combo")