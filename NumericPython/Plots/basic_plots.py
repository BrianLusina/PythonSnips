from matplotlib import pyplot
import numpy as np


height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))

pyplot.plot(height, weight)

pyplot.show()
