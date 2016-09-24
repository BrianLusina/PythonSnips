"""
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"

"""
import re


def maskify(cc):
    return cc if len(cc) <= 4 else re.sub(r'.', r'#', cc[:-4]) + cc[len(cc) - 4:]


print "Testing for maskify(cc) function"
print "Actual:", maskify("4556364607935616"), "Expected:", "############5616", maskify(
    "4556364607935616") == "############5616"
print maskify("64607935616") == "#######5616"
print maskify("1") == "1"
print maskify("") == ""
print maskify("Skippy") == "##ippy"
print maskify("Nananananananananananananananana Batman!") == "####################################man!"
print maskify("123")

greek_alphabet = (
'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
import itertools


def greek_comparator(lhs, rhs):
    m = list(sorted(greek_alphabet))  # m.index(lhs) - m.index(rhs)
    product = list(itertools.product(m))
    return product


print greek_comparator('alpha', 'beta')  # < 0, "result should be negative"
print greek_comparator('chi', 'chi')
print greek_comparator('upsilon', 'rho')

m = list(sorted(greek_alphabet))
for element in itertools.product(m):
    print element

"""
You will be given a list of strings which will include both integers and characters.

Return a list of length 2 with lst[0] representing the mean of the integers to a single decimal place. There will always be 10 integers and 10 characters. Create a single string with the characters and return it as lst[1] while maintaining the original order.

lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']
Here is an example of your return

[3.6, 'udiwstagwo']

"""


def mean(lst):
    nums = [float(i) for i in lst if i.isdigit()]
    strings = "".join([x for x in lst if not x.isdigit()])
    return [round(sum(nums) / len(nums)), strings]


lst1 = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']
print(mean(lst1), [3.6, 'udiwstagwo'])
lst2 = ['0', 'c', '7', 'x', '6', '2', '3', '5', 'w', '7', '0', 'y', 'v', 'u', 'h', 'i', 'n', 'u', '0', '0']
print(mean(lst2), [3.0, 'cxwyvuhinu'])
lst3 = ['0', 'u', 'a', 'y', '0', 'a', '9', 'q', '3', 'v', 'g', '7', '6', '4', 'y', 'd', '8', '6', '0', 'd']
print(mean(lst3), [4.3, 'uayaqvgydd'])
lst4 = ['s', 'n', '9', 'l', '0', 'm', 'i', 'z', '9', '7', 'y', '4', 'z', '3', '3', 'k', '4', '1', '0', 'k']
print(mean(lst4), [4.0, 'snlmizyzkk'])
lst5 = ['5', 'v', 'u', 'k', '8', '4', '9', 'b', '9', 'g', '5', 'z', '3', 'f', '6', 'u', 'i', '6', '6', 't']
print(mean(lst5), [6.1, 'vukbgzfuit'])
