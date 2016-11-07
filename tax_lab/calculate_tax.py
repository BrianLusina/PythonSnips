TAX_RATES = {0: range(0, 1001), 10: range(1000, 10001), 15: range(10000, 20201), 20: range(20200, 30751),
             25: range(30750, 50001)}
#, 30: 50000


def calculate_tax(people_sal):
    for tax in TAX_RATES:
        diff = max(TAX_RATES[tax]) - min(TAX_RATES[tax])
        print(diff)

print(calculate_tax({
    "Alex": 0,
    "James": 2490,
    "Kinuthia": 15352.5
}))


