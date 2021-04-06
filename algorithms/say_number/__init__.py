def say(number, recurse=False):
    """
    Pseudo: create the variables that contain the string literals for the numbers
    ones_teens: key,value pair with the integer and its word, from 0-20
    tens: key value pairs for tens, 20, 30, 40...
    thousands, millions, billions, trillions: contains, well, as the names suggests

    Conditionals are used to check for validation and obtain string literals. If the number is out of
    range, i.e, less than 0 or greater than a trillion, then an Attribute Error is raised.

    if number is less than twenty, return that number after recursion(calling say() again)

    if number is less than 100,
        check if the number is divisible by 10, return the English word, found in tens dictionary
        else: return the tens part and the ones part

    if number is less than 1000,
        check if divisible by 100, if so, return the English word of the hundreds part
        else: return the hundreds part and the recursed tens part and ones part

    same logic applies for millions, billions and trillions

    :param number: number to say
    :param recurse: Whether to call this same function again
    :return: the number in words
    """
    ones_teens = dict(enumerate(('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                                 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                                 'sixteen', 'seventeen', 'eighteen', 'nineteen')))

    tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
            60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    thousands, millions, billions, trillions = 1e3, 1e6, 1e9, 1e12

    if number < 0:
        raise ValueError('number is negative')
    if number >= trillions:
        raise ValueError('number is too large: %s' % str(number))

    if number < 20:
        return ones_teens[number] if not recurse else 'and ' + ones_teens[number]

    if number < 100:
        if number % 10 == 0:
            return tens[number]
        return tens[number // 10 * 10] + '-' + ones_teens[number % 10]

    if number < thousands:
        if number % 100 == 0:
            return ones_teens[number // 100] + ' hundred'

        return ones_teens[number // 100] + ' hundred and ' + say(number % 100)

    if number < millions:
        if number % thousands == 0:
            return say(number // thousands) + ' thousand'
        return say(number // thousands) + ' thousand ' + say(number % thousands, True)

    if number < billions:
        if number % millions == 0:
            return say(number // millions) + ' million'
        return say(number // millions) + ' million ' + say(number % millions, True)

    if number % billions == 0:
        return say(number // billions) + ' billion'
    return say(number // billions) + ' billion ' + say(number % billions, True)
