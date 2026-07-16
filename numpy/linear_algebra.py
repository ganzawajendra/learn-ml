import numpy as np

# ======================================

# DOT 
# perkalian matrix
# Cara 1 -> np.dot(array1, array2)
# Cara 2 -> array1 @ array2

dotVector_1 = np.array([1, 2, 3])
dotVector_2 = np.array([4, 5, 6])
resultVector = np.dot(dotVector_1, dotVector_2)
print(f"Hasil perkalian 1D matrix: {resultVector}")

dotMatrix2D_2 = np.array([[5, 6], [7, 8]])
dotMatrix2D_1 = np.array([[1, 2], [3, 4]])
result2D = dotMatrix2D_1.dot(dotMatrix2D_2)
print(f"Hasil perkalian 2D matrix:\n {result2D}")

# ======================================

# MATRIX TRANSPOSE
# Cara 1 -> array.T()
# Cara 2 -> np.transpose(array)

transposeMatrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Sebelum transpose\n {transposeMatrix}")

resultTransposeCara1 = transposeMatrix.T
print(f"Hasil setelah transpose cara 1\n {resultTransposeCara1}")

resultTransposeCara2 = np.transpose(transposeMatrix)
print(f"Hasil setelah transpose cara 2\n {resultTransposeCara2}")

# ======================================

# MATRIX INVERS
# matrix harus persegi
# .linalg.inv(array)

inversMatrix = np.array([[1, 2], [5, 6]])
resultInvers = np.linalg.inv(inversMatrix)
print(f"Sebelum invers\n {inversMatrix}")
print(f"Hasil setelah invers\n {resultInvers}")

# ======================================

# MATRIX DETERMINANT
# matrix harus persegi
# .linalg.det(array)

determinantMatrix = np.array([[4, 7], [2, 6]])
resultDeterminant = np.linalg.det(determinantMatrix)
print(f"Sebelum determinant\n {determinantMatrix}")
print(f"Hasil setelah determinant\n {resultDeterminant}")