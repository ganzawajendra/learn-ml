import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
# 2D array
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# 3D array
arr3 = np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]], [[5, 5, 5], [6, 6, 6]]])

# ======================================

# SHAPE
# returns the size of the array in each dimension.
print(arr1)
print(arr1.shape)

print(arr2)
print(arr2.shape)

print(arr3)
print(arr3.shape)

# ======================================

# NDIM
# return number of dimension of the array
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# ======================================

# SIZE
# return number of elements in the array
print(arr1.size)
print(arr2.size)
print(arr3.size)

# ======================================

# DTYPE
# return data type of elements in the array
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)