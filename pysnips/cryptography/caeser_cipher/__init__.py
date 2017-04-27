import string


class CaesarCipher(object):
    """ Encrypt and decrypt messages using Caesar Cipher. Specify
        the number of letters to shift ( key ). All alphabetical
        characters will be encrypted and decrypted using key.
        All non-alphabetical characters will be included as-is in
        the cipher_text and plaintext. If key is not provided, it
        uses key = 3 by default.
    """

    def __init__(self, key=3):
        """ Initializes Caesar Cipher using specified key.
        :param int key: The number of letters to shift. Default is 3.
        """
        self.key = key % 26

        # dict used for encryption - { plaintext letter : cipher_text letter, ... }
        self.e = dict(zip(string.ascii_lowercase, string.ascii_lowercase[self.key:]
                          + string.ascii_lowercase[:self.key]))

        self.e.update(dict(zip(string.ascii_uppercase, string.ascii_uppercase[self.key:]
                               + string.ascii_uppercase[:self.key])))

        # dict used for decryption - { cipher_text letter : plaintext letter, ... }
        self.d = dict(zip(string.ascii_lowercase[self.key:] + string.ascii_lowercase[:self.key],
                          string.ascii_lowercase))

        self.d.update(dict(zip(string.ascii_uppercase[self.key:] +
                               string.ascii_uppercase[:self.key], string.ascii_uppercase)))

    def encrypt(self, plaintext):
        """Converts plaintext to cipher_text.

        :param str plaintext: The message to encrypt.
        :return: The cipher_text.
        :rtype: str
        """
        return ''.join([self.e[letter]
                        if letter in self.e else letter
                        for letter in plaintext])

    def decrypt(self, cipher_text):
        """ Converts cipher_text to plaintext.

        :param str cipher_text: The message to decrypt.
        :return: The plaintext.
        :rtype: str
        """
        return ''.join([self.d[letter]
                        if letter in self.d else letter
                        for letter in cipher_text])
