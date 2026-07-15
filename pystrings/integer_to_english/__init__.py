def number_to_words_recursion(num: int) -> str:
    if num == 0:
        return "Zero"

    below_ten = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
    ]
    below_twenty = [
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    below_hundred = [
        "",
        "Ten",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]

    # Recursive function to convert numbers to words
    # Handles numbers based on their ranges: <10, <20, <100, <1000, <1000000, <1000000000, and >=1000000000
    def convert_to_words(number: int) -> str:
        if number < 10:
            return below_ten[number]
        if number < 20:
            return below_twenty[number - 10]
        if number < 100:
            return below_hundred[number // 10] + (
                " " + convert_to_words(number % 10) if number % 10 != 0 else ""
            )
        if number < 1000:
            return (
                convert_to_words(number // 100)
                + " Hundred"
                + (" " + convert_to_words(number % 100) if number % 100 != 0 else "")
            )
        if number < 1000000:
            return (
                convert_to_words(number // 1000)
                + " Thousand"
                + (" " + convert_to_words(number % 1000) if number % 1000 != 0 else "")
            )
        if number < 1000000000:
            return (
                convert_to_words(number // 1000000)
                + " Million"
                + (
                    " " + convert_to_words(number % 1000000)
                    if number % 1000000 != 0
                    else ""
                )
            )
        return (
            convert_to_words(number // 1000000000)
            + " Billion"
            + (
                " " + convert_to_words(number % 1000000000)
                if number % 1000000000 != 0
                else ""
            )
        )

    return convert_to_words(num)


def number_to_words_recursion_2(num: int) -> str:
    if num == 0:
        return "Zero"

    # Store the word representations of the numbers from 1 to 19
    below20 = [
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]

    # Store the word representations of tens numbers
    tens = [
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]

    # Store the word representations of thousands numbers
    thousands = ["", "Thousand", "Million", "Billion"]

    # Function to find word representation of a three-digit number
    def represent(n):
        if n == 0:
            return ""
        elif n < 20:
            return below20[n - 1] + " "
        elif n < 100:
            return tens[n // 10 - 2] + " " + represent(n % 10)
        else:
            return below20[n // 100 - 1] + " Hundred " + represent(n % 100)

    # Initialize the result string
    result = ""

    # For each string in thousands
    for t in thousands:
        # If the last three digits are not zero
        if num % 1000 != 0:
            # Get the representation of the three-digit number, append result to it, and
            # store it back in result
            result = represent(num % 1000) + t + " " + result

        # Divide num by 1000 and update num with the quotient
        num //= 1000

    # Return the result string
    return result.strip()


def number_to_words_iterative(num: int) -> str:
    # Handle the special case where the number is zero
    if num == 0:
        return "Zero"

    # Arrays to store words for single digits, tens, and thousands
    ones = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    tens = [
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]
    thousands = ["", "Thousand", "Million", "Billion"]

    # StringBuilder to accumulate the result
    result = ""
    group_index = 0

    # Process the number in chunks of 1000
    while num > 0:
        # Process the last three digits
        if num % 1000 != 0:
            group_result = ""
            part = num % 1000

            # Handle hundreds
            if part >= 100:
                group_result += ones[part // 100] + " Hundred "
                part %= 100

            # Handle tens and units
            if part >= 20:
                group_result += tens[part // 10] + " "
                part %= 10

            # Handle units
            if part > 0:
                group_result += ones[part] + " "

            # Append the scale (thousand, million, billion) for the current group
            group_result += thousands[group_index] + " "
            # Insert the group result at the beginning of the final result
            result = group_result + result
        # Move to the next chunk of 1000
        num //= 1000
        group_index += 1

    return result.strip()


def number_to_words_pair(num: int) -> str:
    if num == 0:
        return "Zero"

    # Dictionary to store words for numbers
    number_to_words_map = {
        1000000000: "Billion",
        1000000: "Million",
        1000: "Thousand",
        100: "Hundred",
        90: "Ninety",
        80: "Eighty",
        70: "Seventy",
        60: "Sixty",
        50: "Fifty",
        40: "Forty",
        30: "Thirty",
        20: "Twenty",
        19: "Nineteen",
        18: "Eighteen",
        17: "Seventeen",
        16: "Sixteen",
        15: "Fifteen",
        14: "Fourteen",
        13: "Thirteen",
        12: "Twelve",
        11: "Eleven",
        10: "Ten",
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
    }

    for value, word in number_to_words_map.items():
        # Check if the number is greater than or equal to the current unit
        if num >= value:
            # Convert the quotient to words if the current unit is 100 or greater
            prefix = (number_to_words_pair(num // value) + " ") if num >= 100 else ""

            # Get the word for the current unit
            unit = word

            # Convert the remainder to words if it's not zero
            suffix = "" if num % value == 0 else " " + number_to_words_pair(num % value)

            return prefix + unit + suffix

    return ""
