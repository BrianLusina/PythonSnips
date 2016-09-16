from urllib.request import urlretrieve


# store the url in a variable for retrieval
wine_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

urlretrieve(wine_url, "red_wine.csv")

