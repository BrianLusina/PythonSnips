## Python String Constants

I am using the string constants: `string.ascii_lowercase` and `string.ascii_uppercase` to build the cipher map. The Caesar Cipher only converts alphabetical characters and these constants provide a nice list of the characters.

## Zip Function in Python

The `zip` function in Python is particularly useful when combined with dictionaries, but is useful anytime you have multiple iterable sequences and you want to combine them to form a single list of tuples. I am using the zip function to build the cipher map for the Caesar Cipher. For encryption, `zip` combines the following lists into a list of tuples for a Caesar Cipher key of 3. It does this for both lower and uppercase letters and for decryption as well, but I am just showing it for encryption of lowercase letters.

    Before Zip: ['a','b','c','d', ... ,'x','y','z'] and ['d','e','f','g', ... ,'a','b','c']

    After Zip: [('a','d'),('b','e'),('c','f'),('d','g'), ... ,('x','a'),('y','b'),('z','c')]
    
## Python Dictionaries

Python dictionaries can be created from a sequence of key-value pairs, and that is exactly what the zip function is providing. I build a dictionary based on the list of tuples created by the zip function in Python. The encryption dictionary is created as such.

    e = dict(('a','d'),('b','e'),('c','f'),('d','g'), ... ,('x','a'),('y','b'),('z','c'))

    e = {'a':'d','b':'e','c':'f','d':'g', ... , 'x':'a','y':'b','z':'c'}

This provides the encryption lookup for each lowercase letter in the plaintext message.

## List Comprehensions

The actual encryption and decryption are done using list comprehensions. Here is the list comprehension for encryption.
```python
def encrypt(self, plaintext):
    return ''.join([self.e[letter]
                    if letter in self.e else letter
                    for letter in plaintext])
```
This boils down to looping through each character in the plaintext and checking to see if the character is in the encryption dictionary. If it is, it adds the encrypted value to the ciphertext. If not, it just passes the character as-is into the ciphertext. The list comprehension creates a list and `''.join(...)` creates a string based on that list.

