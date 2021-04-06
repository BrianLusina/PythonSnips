import pandas as pd

# loads files
# np.loadtxt()

# loads data of mixed  datatypes
# np.genfromtxt()
"""
There is also another function np.recfromcsv() that behaves similarly to np.genfromtxt(), except that its default
dtype is None
"""
# Assign the filename: file
file = open('TRANS.csv')

# Read the file into a DataFrame: df
df = pd.read_csv(file)

print(df.head())
