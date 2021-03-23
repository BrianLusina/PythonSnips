GIFTS = ['twelve Drummers Drumming',
         'eleven Pipers Piping',
         'ten Lords-a-Leaping',
         'nine Ladies Dancing',
         'eight Maids-a-Milking',
         'seven Swans-a-Swimming',
         'six Geese-a-Laying',
         'five Gold Rings',
         'four Calling Birds',
         'three French Hens',
         'two Turtle Doves',
         'a Partridge in a Pear Tree']

ORDINAL = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
           'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']


def sing():
    return verses(1, 12)


def verse(num):
    # last gift
    gifts = GIFTS[-num:]
    if len(gifts) > 1:
        gifts[:-1] = [", ".join(gifts[:-1])]
    gifts = ", and ".join(gifts)
    return "On the {} day of Christmas my true love gave to me, {}.\n".format(ORDINAL[num], gifts)


def verses(start, stop):
    return "".join(verse(n) + "\n" for n in range(start, stop + 1))

