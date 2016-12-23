from data_science.wine_data import RedWineData

red_wine = RedWineData()
wines = red_wine.extract_data()
# red_wine.store_data()

# selecting a particular data item in the matrix
print(wines[2, 3])
# output 2.3

# slicing
print(wines[0:3, 3])
# or wines[:3,3]
# output [ 1.9  2.6  2.3]

# select the entire 4th column
print(wines[:, 3])
# output
# [ 1.9  2.6  2.3 ...,  2.3  2.   3.6]

# extract entire row
print(wines[3, :])
