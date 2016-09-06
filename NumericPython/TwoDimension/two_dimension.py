import numpy as np

base = [[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]

# create a 2D Numpy array from base. Print out the type of np_baseball.
np_base = np.array(base)
print(np_base, type(np_base))

# Print out the shape attribute of np_baseball. Use np_baseball.shape.
print(np_base.shape)
# baseball is available as a regular list of lists

# Create np_baseball (2 cols)
np_baseball = np.array(base)

# Print out the 50th row of np_baseball
print(np_baseball[49, :])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:, 2]

# Print out height of 124th player
print(np_baseball[1, 124])
