TAX LAB Country X calculates tax for its citizens using a graduated scale rate as shown below:

Yearly Income: 0 - 1000

Tax Rate: 0%

Yearly Income: 1,001 - 10,000

Tax Rate: 10%

Yearly Income: 10,001 - 20,200

Tax Rate: 15%

Yearly Income: 20,201 - 30,750

Tax Rate: 20%

Yearly Income: 30,751 - 50,000

Tax Rate: 25%

Yearly Income: Over 50,000

Tax Rate: 30%

Write a Python function named calculate_tax that will take as an argument, a dictionary containing key-value pairs of
people's names as the keys and their yearly incomes as the values.

The function should return a dictionary containing key-value pairs of the same people’s names as keys and their yearly
tax bill as the values. For example, given the sample input below:

{ ‘Alex’: 500, ‘James’: 20500, ‘Kinuthia’: 70000 } The output would be as follows:

{ ‘Alex’: 0, ‘James’: 2490, ‘Kinuthia’: 15352.5 } The tax for James would be calculated as follows:

The first 1000 (1000 - 0)

Calculation: 1,000 * 0%

Tax: 0

The next 9000 (10,000 - 1,000)

Calculation: 9,000 * 10%

Tax: 900

The next 10,200 (20,200 -10,000)

Calculation: 10,200 * 15%

Tax: 1530

The remaining 300 (20,500 - 20,200)

Calculation: 300 * 20%

Tax: 60

Total Income: 20,500

Total Tax: 0 + 900 + 1530 + 60 = 2490

