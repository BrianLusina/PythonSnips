"Class to test truths of functions"
class Test(object):
    def __init__(self,n):
        self.n = n

    @staticmethod
    def test_function(actual,expected):
        print "Test for " + str(actual) + " passed " if actual == expected else "Test for " + str(actual) + " failed, expected " + str(expected)

line="---------------------------------------------------------------------------"
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
print line
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
import string

def sc(s):
    ret=[]
    for c in s:
        if c.isupper():
            if chr(ord(c)+32) in s:
                ret.append(c)
        elif c.islower():
            if chr(ord(c)-32) in s:
                ret.append(c)
    return ''.join(ret)

import test
print(sc("Aab"), "Aa")
print(sc("AabBc"), "AabB")
print(sc("SONson"), "SONson")
print(sc("FfAaTtHhEeRr"), "FfAaTtHhEeRr")  
print(sc("SONsonfather"), "SONson")  
print(sc("sonfather"), "")
print(sc("DONKEYmonkey"), "ONKEYonkey") 
print(sc("monkeyDONKEY"), "onkeyONKEY") 
print(sc("BANAna"), "ANAna")
print line

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
print line
print zebulansNightmare("goto_next_kata")
print line

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
print line


"""
Suzuki needs help lining up his students!

Today Suzuki will be interviewing his students to ensure they are progressing in their training. He decided to schedule the interviews based on the length of the students name in descending order. The students will line up and wait for their turn.

You will be given a string of student names. Sort them and return a list of names in descending order.

Here is an example input:

string = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'
Here is an example return from your function:

 lst = ['Takehiko',
        'Takayuki',
        'Takahiro',
        'Takeshi',
        'Takeshi',
        'Takashi',
        'Tadashi',
        'Takeo',
        'Takao']
Names of equal length will be returned in descending alphabetical order such that:

string = "xxa xxb xxc xxd xa xb xc xd"
Returns

['xxd', 'xxc', 'xxb', 'xxa', 'xd', 'xc', 'xb', 'xa']
"""
def lineup_students(string):
    return sorted(string.split(), key=lambda x: (len(x), x), reverse=True)

#lineup_students = lambda s: sorted(s.split(), key=lambda x: (len(x), x), reverse=True)

s1 = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'

lst1 = ['Takehiko',
        'Takayuki',
        'Takahiro',
        'Takeshi',
        'Takeshi',
        'Takashi',
        'Tadashi',
        'Takeo',
        'Takao']
Test.test_function(lineup_students(s1), (lst1))

s2 = '''Michio Miki Mikio Minori Minoru Mitsuo Mitsuru Nao Naoki Naoko Noboru Nobu Nobuo ,Nobuyuki Nori Norio Osamu Rafu Raiden Ringo Rokuro Ronin Ryo Ryoichi Ryota Ryozo Ryuichi Ryuu Saburo Sadao Samuru Satoru Satoshi Seiichi Seiji Senichi Shichiro Shig Shigekazu Shigeo Shigeru Shima Shin Shinichi Shinji Shiro Shoichi Shoji Shuichi Shuji Shunichi Susumu Tadao Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi Takumi Tama Tamotsu Taro Tatsuo Tatsuya Teruo Tetsip Tetsuya Tomi Tomio Toru Toshi Toshiaki Toshihiro Toshio Toshiyuki Toyo Tsuneo Tsutomu Tsuyoshi Uyeda Yasahiro Yasuhiro Yasuo Yasushi Yemon Yogi Yoichi Yori Yoshi Yoshiaki Yoshihiro Yoshikazu Yoshimitsu Yoshinori Yoshio Yoshiro Yoshito Yoshiyuki Yuichi Yuji Yuki'''

lst2 =['Yoshimitsu', 'Yoshiyuki', 'Yoshinori', 'Yoshikazu', 'Yoshihiro',
 'Toshiyuki', 'Toshihiro', 'Shigekazu', ',Nobuyuki', 'Yoshiaki', 'Yasuhiro',
 'Yasahiro', 'Tsuyoshi', 'Toshiaki', 'Takehiko', 'Takayuki', 'Takahiro',
 'Shunichi', 'Shinichi', 'Shichiro', 'Yoshito', 'Yoshiro', 'Yasushi',
 'Tsutomu', 'Tetsuya', 'Tatsuya', 'Tamotsu', 'Takeshi', 'Takeshi', 'Takashi',
 'Tadashi', 'Shuichi', 'Shoichi', 'Shigeru', 'Senichi', 'Seiichi', 'Satoshi',
 'Ryuichi', 'Ryoichi', 'Mitsuru', 'Yuichi', 'Yoshio', 'Yoichi', 'Tsuneo',
 'Toshio', 'Tetsip', 'Tatsuo', 'Takumi', 'Susumu', 'Shinji', 'Shigeo',
 'Satoru', 'Samuru', 'Saburo', 'Rokuro', 'Raiden', 'Noboru', 'Mitsuo',
 'Minoru', 'Minori', 'Michio', 'Yoshi', 'Yemon', 'Yasuo', 'Uyeda', 'Toshi',
 'Tomio', 'Teruo', 'Takeo', 'Takao', 'Tadao', 'Shuji', 'Shoji', 'Shiro',
 'Shima', 'Seiji', 'Sadao', 'Ryozo', 'Ryota', 'Ronin', 'Ringo', 'Osamu',
 'Norio', 'Nobuo', 'Naoko', 'Naoki', 'Mikio', 'Yuki', 'Yuji', 'Yori', 'Yogi',
 'Toyo', 'Toru', 'Tomi', 'Taro', 'Tama', 'Shin', 'Shig', 'Ryuu', 'Rafu',
 'Nori', 'Nobu', 'Miki', 'Ryo', 'Nao']

Test.test_function(lineup_students(s2), (lst2))

s3 = 'Yoshiro Yoshiro Tsuyoshi Shoichi Naoko Yori Takayuki Tsutomu Shigeo'
lst3 = ['Tsuyoshi', 'Takayuki', 'Yoshiro', 'Yoshiro', 'Tsutomu', 'Shoichi', 'Shigeo', 'Naoko', 'Yori']
Test.test_function(lineup_students(s3), (lst3))
print line
