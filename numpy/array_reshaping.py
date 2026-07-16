import numpy as np

arrReshaping1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# ======================================

# DARI 1D MENJADI 2D
# CARA 1 -> .reshape(baris, kolom)
shape1 = arrReshaping1.reshape(4, 3)
print(shape1)

# CARA 2 -> np.reshape(array, (baris, kolom))
shape2 = np.reshape(arrReshaping1, (4, 3))
print(shape2)

# ======================================

# DARI 1D MENJADI 3D
# CARA 1 -> .reshape(jumlah_matriks, baris, kolom)
shape3 = arrReshaping1.reshape(2, 3, 2)
print(shape3)

# CARA 2 -> np.reshape(array, (jumlah_matriks, baris, kolom))
shape3 = np.reshape(arrReshaping1, (2, 3, 2))
print(shape3)

# ======================================

# OTOMATIS DENGAN -1
# Menghitung otomatis jumlah kolom dengan -1
# CARA 1 -> .reshape(baris, kolom)
shape4 = arrReshaping1.reshape(3, -1)
print(shape4)

# CARA 2 -> np.reshape(array, (jumlah_matris, baris, kolom))
shape5 = np.reshape(arrReshaping1, (2, 2, -1))
print(shape5)