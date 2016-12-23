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
# output [ 11.2     0.28    0.56    1.9     0.075  17.     60.      0.998   3.16
# 0.58    9.8     6.   ]

# select all rows and cols
print(wines[:, :])
"""
output
[[  7.4     0.7     0.    ...,   0.56    9.4     5.   ]
 [  7.8     0.88    0.    ...,   0.68    9.8     5.   ]
 [  7.8     0.76    0.04  ...,   0.65    9.8     5.   ]
 ...,
 [  6.3     0.51    0.13  ...,   0.75   11.      6.   ]
 [  5.9     0.645   0.12  ...,   0.71   10.2     5.   ]
 [  6.      0.31    0.47  ...,   0.66   11.      6.   ]]
"""

# assigning values to arrays
# assign the data item at row 1, col 5 to 10
wines[1, 5] = 10

# overwrite the entire 11th col to 50
wines[:, 10] = 50

# extract the entire 3rd row
third_wine = wines[3, :]

# data type
dtype = wines.dtype
print(dtype)

# changing data types from float to int
wines.astype(int)
print(wines)
print(wines.dtype)
