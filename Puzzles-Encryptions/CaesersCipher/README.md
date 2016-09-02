Python String Constants

One of the really useful things I love about Python is its string constants. I find these extremely useful in my course assignments. As you can see in the CaesarCipher Class, I am using the string constants: string.ascii_lowercase and string.ascii_uppercase to build the cipher map. The Caesar Cipher only converts alphabetical characters and these constants provide a nice list of the characters. There is also string.ascii_letters, string.punctuation, and string.whitespace that I use in my unit tests to make sure non-alphabetical characters are passed through as-is and encryption is working correctly for all letters. I realize this is a basic feature of Python, but I find I use string constants a lot in Python.

Zip Function in Python

The zip function in Python is particularly useful when combined with dictionaries, but is useful anytime you have multiple iterable sequences and you want to combine them to form a single list of tuples. I am using the zip function to build the cipher map for the Caesar Cipher. For encryption, zip combines the following lists into a list of tuples for a Caesar Cipher key of 3. It does this for both lower and uppercase letters and for decryption as well, but I am just showing it for encryption of lowercase letters.

