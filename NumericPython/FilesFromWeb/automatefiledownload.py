from urllib.request import urlretrieve


# store the url in a variable for retrieval
url = "https://www.kaggle.com/benhamner/y-combinator-companies/downloads/companies.csv"

urlretrieve(url, "companies.csv")
