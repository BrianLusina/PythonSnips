from data_science.data_download import DataDownload
import pandas as pd
from matplotlib import pyplot as plt

# store the url in a variable for retrieval
wine_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

red_wine = DataDownload(wine_url, "red_wine.csv")
red_wine.download()

# Read file into a DataFrame and print its head
df = pd.read_csv('red_wine.csv', sep=';')
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()
