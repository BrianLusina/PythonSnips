def calculate_total(books, price_thus_far=0.):
    """
    Calculates the total amount that one can get from the books. Should return the least discount
    one can get from the book titles
    :param books: list of books
    :param price_thus_far: price so far
    :return: least price from the set of books purchased
    """
    if not books:
        return price_thus_far

    groups = list(set(books))
    min_price = float("inf")

    for x in range(len(groups)):
        # create a copy of the books
        books_remaining = books[:]

        for y in groups[: x + 1]:
            books_remaining.remove(y)

        # calculate the price on the remaining books
        price = calculate_total(books_remaining, price_thus_far + group_price(x + 1))

        # get the minimum price discount
        min_price = min(min_price, price)

    return min_price


def group_price(size):
    """
    Calculates group price of books
    :param size: size of the books 
    :return: price of the group of books
    """
    discounts = [0, .05, .1, .2, .25]
    if not (0 < size <= 5):
        ValueError("Size must be in range 1...{}".format(len(discounts)))
    return 8 * size * (1 - discounts[size - 1])
