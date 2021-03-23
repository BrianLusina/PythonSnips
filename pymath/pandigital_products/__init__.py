def pandigital_products(limit=10000):
    """
    Find all pandigital products for the given upper limit
    :param limit: upper limit, defaults to 10000
    :type limit int
    :return: sum of all pandigital products
    :rtype: int
    """
    products = set()
    pandigital = "123456789"

    for x in range(limit):
        for y in range(limit):
            product = x * y
            num_str = "".join(sorted(str(x) + str(y) + str(product)))
            if num_str == pandigital:
                products.add(product)

    return sum(products)


if __name__ == "__main__":
    upper_limit = 10000
    pan_products = pandigital_products(upper_limit)
    print(f"Sum of pandigital products for upper limit of {upper_limit} is {pan_products}")
