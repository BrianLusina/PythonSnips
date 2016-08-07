line="---------------------------------------------------------------------------"
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
