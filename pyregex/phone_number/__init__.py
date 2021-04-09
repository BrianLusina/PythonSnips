import re


class Phone(object):
    """
    Evaluates phone numbers and returns a neat format of the number
    Also gets the area code and returns it from the phone number.
    If the phone number is invalid, it will return 0000000000 instead of the invalid phone number
    """

    def __init__(self, phone_number):
        """
        Returns a Phone object
        :param phone_number: Phone number to evaluate
        The number is cleaned before initialized it
        """
        self.number = self._clean_number(phone_number)

    def area_code(self):
        """
        Fetches the area code from the number
        :return: String with 3 digits as the area code
        :rtype:str
        """
        return self.number[:3]

    def exchange_code(self):
        """
        Returns the exchange code, the next 3 digits from area code
        :return:
        """
        return self.number[3:6]

    def subscriber_number(self):
        """
        Returns the subscriber number from the number provided.
        :return: subscriber number, which is the last 4 digits
        """
        return self.number[-4:]

    def pretty(self):
        """
        'Prettifies' the number into (AREA-CODE) 3DIGITS-REST_OF_NUMBER
        :return: Neatly formatted number as a string
        :rtype:str
        """
        return "(%s) %s-%s" % (
            self.area_code(),
            self.exchange_code(),
            self.subscriber_number()
        )

    def _clean_number(self, number):
        """
        Cleans the number before normalizing it, replaces any string that is not a number with an empty string
        :param number: The number to clean
        :return: a clean and normalized number
        """
        return self._normalize(
            re.sub(r"[^\d]", "", number)
        )

    @staticmethod
    def _normalize(number):
        """
        Normalizes the number and checks if the number is valid
        :return: Number if the number follows given rules
        :rtype:str
        """
        valid = len(number) == 10 or len(number) == 11 and number.startswith("1")

        if valid:
            # return 10 digits, excluding the first number
            return number[-10:]
        else:
            return "0" * 10
