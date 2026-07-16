import numpy as np

# membuat vector dan array multidimensi (matrix)
arr1D = np.array([1,2,3,4,5])
# print(arr1D)
arr2D = np.array([[1,2,3,4], [5,6,7,8]])
# print(arr2D)
arr3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(arr3D)

# ======================================

# MEMBUAT VEKTOR DENGAN RANGE
# .arange([start], [stop], step, dtype)
arrRange1 = np.arange(1, 10, 0.5)
print(arrRange)

# KOMBINASI DENGAN KONDISIONAL
arrRange2 = np.arange(0, 20, 3)
conditional = arrRange2[arrRange2 > 10]
# print(conditional)

# ======================================

# MEMBUAT LINEAR SPACE 
# .linspage([start], [stop], num, endpoint, retstep, dtype, axis)
arrLin1 = np.linspace(1, 10, 4)
# print(arrLin1)

# endpoint (default True) -> opsional
arrLin2 = np.linspace(1, 20, 5, endpoint=False) # -> jika False, [stop] iterasi tidak include
# print(arrLin2)

# retstep (default False) -> opsional
arrLin3 = np.linspace(1, 20, 5, True, retstep=True) # -> jika True, return (samples, step)
# print(arrLin3)

# dtype (np.int8, np.int16, np.int32, np.int64, np.unit16, np.float16, np.bool_ dst) -> opsional
arrLin4 = np.linspace(1, 20, 5, True, False, dtype=np.int8)
# print(arrLin4)

# axis (default 0) -> opsional
# 2 jalur 1-20 dan 10-40
start5 = [1, 10]
stop5 = [20, 40]
arrLin5 = np.linspace(start5, stop5, 5, True, False, np.int8, axis=-1)
# print(arrLin5)

# ======================================

# MATRIX DENGAN NILAI 0
# .zeros(shape, dtype)
arrZeros1 = np.zeros(5)
# print(arrZeros1)

# shape(x, y) -> besaran matrix yang dibangun
arrZeros2 = np.zeros((5,3))
# print(arrZeros2)
# 3D array
arrZeros3 = np.zeros((2, 2, 3))
# print(arrZeros3)

# dtype (np.int8, np.int16, np.int32, np.int64, np.unit16, np.float16, np.bool_ dst) -> opsional
arrZeros4 = np.zeros((5,3), dtype=np.int8)
# print(arrZeros4)

# ======================================

# MATRIX DENGAN NILAI 1
# .ones(shape, dtype)
arrOnes1 = np.ones(3)
# print(arrOnes1)

# shape(x, y) -> besaran matrix yang dibangun
arrOnes2 = np.ones((3, 4))
# print(arrOnes2)
arrOnes3 = np.ones((2, 2, 4))
# print(arrOnes3)

# dtype (np.int8, np.int16, np.int32, np.int64, np.unit16, np.float16, np.bool_ dst) -> opsional
arrOnes4 = np.ones((3, 4), dtype=np.float16)
# print(arrOnes4)

# ======================================

# MATRIX IDENTITAS
# .identity(n, dtype)
arrIden1 = np.identity(5)
# print(arrIden1)

# dtype (np.int8, np.int16, np.int32, np.int64, np.unit16, np.float16, np.bool_ dst) -> opsional
arrIden2 = np.identity(5, dtype=np.int8)
print(arrIden2)