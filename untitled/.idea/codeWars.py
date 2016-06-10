"""
Reach Me and sum my digits
"""
"""
def sumDig(initVal,patternL,nthTerm):
    x,newL,nextVal=0,[initVal],0
    n = [sum(patternL[0:i + 1]) for i in range(0, len(patternL), 1)]
    m = [n[len(n)-1] +i for i in range(0,len(patternL),1)]
    print n
    print m
print(sumDig(10,[2,1,3],6))
"""

def sumDig_nthTerm(a, ds, n):
    n -= 1
    n_cycles = n / len(ds)
    print n_cycles
    rem = n % len(ds)
    print rem
    term = a + n_cycles * sum(ds) + sum(ds[:rem])
    print term
    return sum(map(int, str(term)))

print sumDig_nthTerm(10,[2,1,3],6)

"""
For every positive integer N, there exists a unique sequence starting with 1 and ending with N and such that every number
in the sequence is either the double of the preceeding number or the double plus 1.

For example, given N = 13, the sequence is [1, 3, 6, 13], because . . . :

 3 =  2*1 +1
 6 =  2*3
 13 = 2*6 +1
Write a function that returns this sequence given a number N. Try generating the elements of the resulting list in ascending order, i.e.,
without resorting to a list reversal or prependig the elements to a list.

test.assert_equals(climb(13), [1, 3, 6, 13])
"""

def climb(n):
    c,newL,nRange =0,[],list(range(1,n+1))
    print "The range is " + str(nRange)
    #if n is odd
    if n == 1 or n ==0:
        return newL.append(n)
    if n%2 !=0:
        i = (n-1)/2
        newL.append(i)
        #i is now even
        if i%2==0:
            i = i/2
            newL.append(i)
        newL = list(reversed(newL))
    #else if n is even
    else:
        i = (n)/2
        newL.append(i)
        #i is now odd
        if i%2 !=0:
            i = (i-1)/2
            newL.append(i)

        newL = list(reversed(newL))
    print "New List is " + str([1] + newL + [n])

print climb(2)

"""
This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version
Task:
Every uppercase letter is Father, The corresponding lowercase letters is the Son.
Give you a string s, If the father and son both exist, keep them.
If it is a separate existence, delete them. Return the result.
For example:
sc("Aab") should return "Aa"
sc("AabBc") should return "AabB"
sc("AaaaAaab") should return "AaaaAaa"(father can have a lot of son)
sc("aAAAaAAb") should return "aAAAaAA"(son also can have a lot of father ;-)
"""
from collections import Counter
def sc(s):
    sl = s.lower()
    if len(s) ==2 and sl[0] == sl[1]:
        return s
    elif len(s) == 2 and sl[0] != sl[1]:
        return ""
    elif len(s) ==1:
        return ""
    else:
        for i in sl:
            if sl.count(i) < 2:
                n= sl.translate(None,i)
        return n

"""
        count = Counter(s)
        n = [i for i in s if 1 < count[i]]
        print n
        return "".join(n)
"""
print sc("BANAna")

"""
Zebulan has worked hard to write all his python code in strict compliance to PEP8 rules. In this kata, you are a mischevious hacker that has set out to sabatoge all his good code.

Your job is to take PEP8 compatible function names and convert them to camelCase. For example:

zebulansNightmare('camel_case') == 'camelCase'
zebulansNightmare('zebulans_nightmare') == 'zebulansNightmare'
zebulansNightmare('get_string') == 'getString'
zebulansNightmare('convert_to_uppercase') == 'convertToUppercase'
zebulansNightmare('main') == 'main'
"""
def zebulansNightmare(functionName):
    #replace the underscore with a space to create separate words and split them into a list
    fn = functionName.replace("_"," ").split()
    fLet=""
    #add first element to a new list
    out = [fn[0]]
    #take only the 2nd and consecutive elements
    for i in fn[1:]:
        #capitalize the first letter only of each word
        fLet = i.title()
        #add each new word to the list
        out.append(fLet)
    #return this new list
    return "".join(out)

print zebulansNightmare("goto_next_kata")


"""
Write a function that rearranges an interger into its largest possible value.

super_size(123456) # 654321
super_size(105)    # 510
super_size(12)     # 21
If the argument passed through is single digit or is already the maximum possible integer,
your function should simply return it.
"""
def super_size(n):
    out = [i for i in str(n)]
    m = int("".join(list(sorted(out))[::-1]))
    return m
print super_size(2150)


"""
Suzuki is the master monk of his monastery so it is up to him to ensure the kitchen is operating at full capacity to
feed his students and the villagers that come for lunch on a daily basis.
This week there was a problem with his deliveries and all the vegetables became mixed up.
There are two important aspects of cooking in his kitchen, it must be done in harmony and nothing can be wasted.
Since the monks are a record keeping people the first order of business is to sort the mixed up vegetables and then
count them to ensure there is enough to feed all the students and villagers.
You will be given a string with the following vegetables:

"cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"
Return a list of tuples with the count of each vegetable in descending order. If there are any non vegetables mixed in discard them.
If the count of two vegetables is the same sort in descending alphabetical order.

(119, "pepper"),
(114, "carrot"),
(113, "turnip"),
(102, "onion"),
(101, "tofu"),
(100, "cabbage"),
(93, "mushroom"),
(90, "cucumber"),
(88, "potato"),
(80, "celery")
"""
from collections import Counter
def count_vegetables(s):
    #split string and store into a list
    count = dict(Counter(s.split()))
    res = [i for i in count.iteritems()]
    return res

print count_vegetables("potato potato tofu kales kales tomatoes celery cucumber cucumber cucumber")


def add_Extra(lst):
    return lst.append(1)

print add_Extra([1,2])
p = [1,2] + [1]
print p