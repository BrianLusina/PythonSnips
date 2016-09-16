from urllib.request import urlretrieve
import pandas as pd

# store the url in a variable for retrieval
wine_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

urlretrieve(wine_url, "red_wine.csv")

# Read file into a DataFrame and print its head
df = pd.read_csv('red_wine.csv', sep=';')
print(df.head())
