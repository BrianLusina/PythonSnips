import numpy as np

# generates random data
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))

# average

# Print mean height (first column)
avg = np.mean(np_city[:, 0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_city[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_city[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_city[:,0], np_city[:,1])
print("Correlation: " + str(corr))
