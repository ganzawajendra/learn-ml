import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# 2D array
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# 3D array
arr3 = np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]], [[5, 5, 5], [6, 6, 6]]])

# [start:stop:step]
# "stop" -> akan berhenti di stop - 1
# ======================================

# FROM INDEX TO THE END
print(arr1[1:])
print(arr2[1:])
print(arr3[1:])

# ======================================

# FROM INDEX TO INDEX
print(arr1[1:4])
print(arr2[1:2])
print(arr3[1:2])

# ======================================

# FROM BEGINNING TO INDEX
print(arr1[:4])
print(arr2[:2])
print(arr3[:2])

# ======================================

# NEGATIVE SLICING -> FROM INDEX FROM THE END TO INDEX FROM END
print(arr1[-6:-2])
print(arr1[-6:])
print(arr1[:-2])

# ======================================

# STEP
print(arr1[1:8:2])
print(arr1[::2])

