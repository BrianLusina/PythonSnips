line = "-----------------------------------------------------------------------------------------------------------"
"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.
eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
"""
def validate_pin(pin):
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
        return True
    else:
        return False

print((validate_pin("1")))

"""
The discussion gets heated and you are cannot risk favoring either of them as this might damage your political standing with either of the two clans the samurai generals belong to. Thus, the only thing left to do is find what the common ground of what they are saying is.

Compare the proposals using the function commonGround(string a, string b) that outputs a string containing the words in string a that also occur in string b.

Each word in the resulting string shall occur once, and the order of the words follow the order of the first occurence of each word in the second string.
If they are saying nothing in common, kill both samurai and blame a ninja. (output "death")
"""


def common_ground(s1, s2):
    lst = []
    for w in s2.split():
        if w in s1.split() and w not in lst:
            lst.append(w)
    return ' '.join(lst) if lst else "death"

print line
print("Test Cases")
print(common_ground("eat chicken", "eat chicken and rice")) #'eat chicken')
print(common_ground("eat a burger and drink a coke", "drink a coke"))# 'drink a coke')
print(common_ground("aa bb", "aa bb cc"))# "aa bb")
print(common_ground("aa bb cc", "bb cc"))# 'bb cc')
print(common_ground("", "cc dd")) # 'death')
print(common_ground("", ""))#, 'death')
print(common_ground("aa bb", "")) # 'death')
print(common_ground("i like turtles", "what are you talking about"))#'death')
print(common_ground("aa bb", "cc dd"))# 'death')
print(common_ground("aa bb cc", "bb cc bb aa"))#'bb cc aa')

"""
You are the judge at a competitive eating competition and you need to choose a winner!

There are three foods at the competition and each type of food is worth a different amount of points. Points are as follows:

Chickenwings: 5 points
Hamburgers: 3 points
Hotdogs: 2 points
Write a function that helps you create a scoreboard. It takes as a parameter a list of objects representing the participants, for example:

[
  {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
  {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
]
It should return "name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.

[
  {name: "Big Bob", score: 134},
  {name: "Habanero Hillary", score: 98}
]
"""
def scoreboard(lst):
    total,scores,finalLst = 0,{},[]
    if len(lst) == 0:
        return lst
    else:
        for i in lst:
            total= (i.get("chickenwings") * 5)+(i.get("hamburgers") * 3)+(i.get("hotdogs") * 2)
            scores["score"] = total
            scores["name"] = i.get("name")
            finalLst.append(scores.copy())
            newlist = sorted(finalLst, key=lambda k: k['score'],reverse=True)

        return newlist

print line
print(scoreboard([{"name": "Billy The Beast", "chickenwings": 17 , "hamburgers": 7, "hotdogs": 8},
                  {"name": "Habanero Hillary", "chickenwings": 5 , "hamburgers": 17, "hotdogs": 11},
                  {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},
                  {"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}
                  ]))

"""
  [{"name": "Big Bob", "score": 134},
   {"name": "Billy The Beast", "score": 122},
   {"name": "Habanero Hillary", "score": 98},
   {"name": "Joey Jaws", "score": 94}]
"""

print(scoreboard([{"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]))
      #[{"name": "Big Bob", "score": 134}])

print(scoreboard([
    {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},{"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]))
    #[{"name": "Big Bob", "score": 134},{"name": "Joey Jaws", "score": 94}]

print(scoreboard([
    {"name": "Joey Jaws", "chickenwings": 0, "hamburgers": 1, "hotdogs": 1},
    {"name": "Big Bob" , "chickenwings": 1, "hamburgers": 0, "hotdogs": 0}]))
    #[{"name": "Big Bob", "score": 5},{"name": "Joey Jaws", "score": 5}])

print(scoreboard([]), [])

"""
JavaScript provides a built-in parseInt method.

It can be used like this:

parseInt("10") returns 10
parseInt("10 apples") also returns 10
We would like it to return "NaN" (as a string) for the second case because the input string is not a valid number.

You are asked to write a myParseInt method with the following rules:

It should make the conversion if the given string only contains a single integer value (and eventually spaces - including tabs, line feeds... - at both ends)
For all other strings (including the ones representing float values), it should return NaN
It should assume that all numbers are not signed and written in base 10
"""
def my_parse_int(string):
    return int(string) if string.replace(" ","").isdigit() else "NaN"

print line
print(my_parse_int("1")) #1
print(my_parse_int("  1 ")) #1
print(my_parse_int("08")) #8
print(my_parse_int("5 friends"))# "NaN"
print(my_parse_int("16.5")) #"NaN"

print line

"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20
"""
def positive_sum(arr):
    return sum([i for i in arr if i>0])


print(positive_sum([1,2,3,4,5])) #15
print(positive_sum([1,-2,3,4,5]))#13
print(positive_sum([-1,2,3,4,-5]))#9
print(positive_sum([]))#0
print(positive_sum([-1,-2,-3,-4,-5]))#0
print line

"""

Let's look at the following generator:

def gen():
    for i in range(2):
        for j in range(3):
            yield (i, j)
If we print all yielded values, we'll get

(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
For a given parameter list N you must return an iterator, which goes through all possible tuples A, where Ai changes from 0 to Ni.
"""
def multiiter(*args):
    m = [i for i in args]
    lst = []
    if len(m) ==1:
        for i in range(m[0]):
            yield (i,)
    elif len(args) == 2:
        for i in range(m[0]):
            for x in range(m[1]):
                yield(i,x)

print list((multiiter(2,3)))

"""
Complete function saleHotdogs, function accept 1 parameters:n, n is the number of customers to buy hotdogs, different numbers have different prices (refer to the following table), return a number that the customer need to pay how much money.

+---------------+-------------+
|  numbers n    | price(cents)|
+---------------+-------------+
|n<5            |    100      |
+---------------+-------------+
|n>=5 and n<10  |     95      |
+---------------+-------------+
|n>=10          |     90      |
+---------------+-------------+
"""
def sale_hotdogs(n):
    if n == 0: return 0
    elif n < 5: return n*100
    elif n>=5 and n<10: return n*95
    elif n>=10: return n*90

print line
print sale_hotdogs(0)#0)
print sale_hotdogs(1)#100)
print sale_hotdogs(2)#200)
print sale_hotdogs(3)#300)
print sale_hotdogs(4)#400)
print sale_hotdogs(5)#475)
print sale_hotdogs(9)#855)

print sale_hotdogs(10)#900)
print sale_hotdogs(11)#990)
print sale_hotdogs(100)#9000)


"""
Lucy loves to travel. Luckily she is a renowned computer scientist and gets to travel to international conferences using her department's budget.

Each year, Society for Exciting Computer Science Research (SECSR) organizes several conferences around the world. Lucy always picks one conference from that list that is hosted in a city she hasn't been to before, and if that leaves her with more than one option, she picks the conference that she thinks would be most relevant for her field of research.

Write a function conferencePicker that takes in two arguments:

citiesVisited, a list of cities that Lucy has visited before, given as an array of strings.
citiesOffered, a list of cities that will host SECSR conferences this year, given as an array of strings. citiesOffered will already be ordered in terms of the relevance of the conferences for Lucy's research (from the most to the least relevant).
The function should return the city that Lucy should visit, as a string.

Also note:

You should allow for the possibility that Lucy hasn't visited any city before.
SECSR organizes at least two conferences each year.
If all of the offered conferences are hosted in cities that Lucy has visited before, the function should return 'No worthwhile conferences this year!' (Nothing in Haskell)
Example:

citiesVisited = ['Mexico City','Johannesburg','Stockholm','Osaka','Saint Petersburg','London'];
citiesOffered = ['Stockholm','Paris','Melbourne'];

conferencePicker (citiesVisited, citiesOffered);
// ---> 'Paris'
"""
def conference_picker(citVisited, citOffered):
    citiesToConsider = [x for x in citOffered if x not in citVisited]
    if len(citiesToConsider)==0:
        return "No worthwhile conferences this year!"
    else:
        return citiesToConsider[0]

print line
print conference_picker([], ['Philadelphia', 'Osaka', 'Tokyo', 'Melbourne']) # 'Philadelphia',
print conference_picker([], ['Brussels', 'Madrid', 'London']) # 'Brussels',
print conference_picker([], ['Sydney', 'Tokyo']) # 'Sydney',
print conference_picker(
    ['London', 'Berlin', 'Mexico City', 'Melbourne', 'Buenos Aires', 'Hong Kong', 'Madrid', 'Paris'],
    ['Berlin', 'Melbourne']) # 'No worthwhile conferences this year!',
print conference_picker(
    ['Beijing', 'Johannesburg', 'Sydney', 'Philadelphia', 'Hong Kong', 'Stockholm', 'Chicago', 'Seoul',
     'Mexico City', 'Berlin'], ['Stockholm', 'Berlin', 'Chicago']) # 'No worthwhile conferences this year!',

print conference_picker(
    ['Mexico City', 'Dubai', 'Philadelphia', 'Madrid', 'Houston', 'Chicago', 'Delhi', 'Seoul', 'Mumbai', 'Lisbon',
     'Hong Kong', 'Brisbane', 'Stockholm', 'Tokyo', 'San Francisco', 'Rio De Janeiro'], ['Lisbon', 'Mexico City'])
    #'No worthwhile conferences this year!'
print conference_picker(['Mexico City','Johannesburg','Stockholm','Osaka','Saint Petersburg','London'],['Stockholm','Paris','Melbourne']) #Paris


cV = ['Beijing', 'Johannesburg', 'Sydney', 'Philadelphia', 'Hong Kong', 'Stockholm', 'Chicago', 'Seoul',
     'Mexico City', 'Berlin']
cO = ['Stockholm', 'Berlin', 'Chicago']

citiesToConsider = [x for x in cO if x not in cV]
print citiesToConsider
print line
"""
I always thought that my old friend John was rather richer than he looked, but I never knew exactly how much money he actually had. One day (as I was plying him with questions) he said: "Imagine I have between m and n Zloty (or did he say Quetzal? I can't remember!)

If I were to buy 9 cars costing c each, I'd only have 1 Zlotty (or was it Meticals?) left.

And if I were to buy 7 boats at b each, I'd only have 2 Ringglets (or was it Zlotty?) left.

Could you tell me in each possible case:

how much money f he could possibly have
the cost c of a car
the cost b of a boat?
So, I will have a better idea about his fortune. Note that if m-n is big enough, you might have a lot of possible answers.

Each answer will be given as ["M: f", "B: b", "C: c"] and all the answers as [ ["M: f", "B: b", "C: c"] ... ]. M stands for "Money", B for boats, C for cars.

m and n are positive or null integers with m <= n or m >= n, m and n inclusive.

Examples:

howmuch(1, 100) => [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]]
howmuch(1000, 1100) => [["M: 1045", "B: 149", "C: 116"]]
howmuch(10000, 9950) => [["M: 9991", "B: 1427", "C: 1110"]]
howmuch(0, 200) => [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"], ["M: 163", "B: 23", "C: 18"]]
Explanation of howmuch(1, 100):

In the first answer his possible fortune is 37 so if he buys 7 boats each worth 5 it remains 37 - 7 * 5 = 2, if he buys 9 cars worth 4 each it remains 37 - 9 * 4 = 1. The same with f = 100: 100 - 7 * 14 = 2 and 100 - 9 * 11 = 1.
"""
def howmuch(m, n):
    pass
