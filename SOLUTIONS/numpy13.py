#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
#Output will print dimension and size of each element and array in memory.
import numpy as np

# create a 3x3 matrix with values ranging from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)

# print the matrix
print("Matrix:")
print(matrix)

# print the dimension and size of each element
print("Element dimension and size:")
for element in np.nditer(matrix):
    print(f"Dimension: {element.ndim}, Size: {element.size}")

# print the dimension and size of the array in memory
print("Array dimension and size in memory:")
print(f"Dimension: {matrix.ndim}, Size: {matrix.size}, Memory Usage: {matrix.nbytes} bytes")


