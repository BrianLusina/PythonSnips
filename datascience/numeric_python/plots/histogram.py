import matplotlib.pyplot as plt

values = [1, 2, 3, 3, 3, 4, 4, 346, 6, 537, 53, 75, 76, 4, 64, 86, 4867, 8, 79, 57, 8, 46, 3, 6, 425, 14, 1]
plt.hist(values, bins=5)

# show plot
plt.show()
# cleans it up again
plt.clf()
