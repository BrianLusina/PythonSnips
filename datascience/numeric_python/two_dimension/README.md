# 2D Numpy Arrays

2D numpy arrays can be created from a list of lists from standard Python.

If your 2D Numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways
of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list
of lists.

## regular list of lists

x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

## numpy

import numpy as np np_x = np.array(x)
np_x[:,0]

For regular Python lists, this is a real pain. For 2D Numpy arrays, however, it's pretty intuitive! The indexes before
the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it
tells Python to include all rows.

## 2D Arithmetic

Remember how you calculated the Body Mass Index for all baseball players? Numpy was able to perform all calculations
element-wise. For 2D Numpy arrays this isn't any different! You can combine matrices with single numbers, with vectors,
and with other matrices.

Execute the code below in the IPython shell and see if you understand:

import numpy as np np_mat = np.array([[1, 2],
[3, 4],
[5, 6]])
np_mat * 2 np_mat + np.array([10, 10])
np_mat + np_mat np_baseball is coded for you; it's again a 2D Numpy array with 3 columns representing height, weight and
age.

## 2D Statistics

You now know how to use Numpy functions to a get a better feeling for your data. It basically comes down to importing
Numpy and then calling several simple functions on the Numpy arrays:

import numpy as np x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)
The baseball data is available as a 2D Numpy array with 3 columns (height, weight, age) and 1015 rows. The name of this
Numpy array is np_baseball. After restructuring the data, however, you notice that some height values are abnormally
high. Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called
outliers.