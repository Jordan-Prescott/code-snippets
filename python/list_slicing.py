# List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slice from index 2 to 5
print(numbers[2:6])  # [2, 3, 4, 5]

# Slice from the beginning to index 4
print(numbers[:5])  # [0, 1, 2, 3, 4]

# Slice from index 5 to the end
print(numbers[5:])  # [5, 6, 7, 8, 9]

# Slice with step
print(numbers[::2])  # [0, 2, 4, 6, 8]

# Reverse the list
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Ellipsis slicing
import numpy as np

# Create a 3D numpy array
arr = np.arange(27).reshape(3, 3, 3)

# Use Ellipsis to select all elements in the second row across all dimensions
print(arr[:, 1, :])
print(arr[..., 1, :])  # Same as above
