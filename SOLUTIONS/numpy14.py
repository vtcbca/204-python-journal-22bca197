#Write a NumPy program to get the values and indices of the elements that are bigger than 10 in a given array.

import numpy as np

# create a sample numpy array
arr = np.array([1, 11, 2, 12, 3, 13])

# get the indices of the elements that are greater than 10
indices = np.where(arr > 10)

# get the values of the elements that are greater than 10
values = arr[indices]

# print the indices and values
print("Indices of elements greater than 10:", indices)
print("Values of elements greater than 10:", values)

