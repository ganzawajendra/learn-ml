import numpy as np

# ======================================

# SEED
# Cocok digunakan untuk mempertahankan nilai lama
# Lalu ingin mengembangkan/memperbaiki nilai lama menjadi lebih bagus

np.random.seed(42) # Mengunci angka random di seed(42)
print("Seed 42 dengan random Integer 2: \n", np.random.rand(2))
print("\nSeed 42 dengan random Integer 2 (lanjutan): \n", np.random.rand(2))

np.random.seed(42)
print("\nSeed 42 dengan random Integer 2 (reset): \n", np.random.rand(4))

# ======================================

# RAND & RANDN
# rand -> menghasilkan angka acak desimal antara 0.0 sampai 0.9
# .rand(baris, kolom)
np.random.seed(42)
#  1 Dimensi
print("\nRandom Float 1 Dimensi: \n", np.random.rand(3))
# 2 Dimensi
print("\nRandom Float 2 Dimensi (3x4): \n", np.random.rand(3,4))

# randn -> menghasilkan angka acak yang berpusat di 0 dengan Standar Deviasi (STD) 1
# nilai bisa -1 sampai +1, semakin jauh dengan 0 akan semakin langka (kemunculannya)
# .rand(baris, kolom)
np.random.seed(42)
#  1 Dimensi
print("\nRandom Float Normal 1 Dimensi: \n", np.random.randn(3))
# 2 Dimensi
print("\nRandom Float Normal 2 Dimensi (3x4): \n", np.random.randn(3,4))

# ======================================

# RANDINT
# randint -> menghasilkan angka acak integer (bulat) antara 1-10
# .randint(low, high, size)
np.random.seed(42)
# 1 Dimensi
print("\nRandom Integer 1 Dimensi Angka Acak (1-9) : \n", np.random.randint(1, 10)) # Mengacak 1-9
print("\nRandom Integer 1 Dimensi 0-4 Diulang 6 Kali: \n", np.random.randint(5, size=6)) # Mengacak 0-4 diulang sebanyak 6 kali
# 2 Dimensi
print("\nRandom Integer 2 Dimensi Size 2x3 : \n", np.random.randint(50, 100, size=(2,3))) # Mengacak 1-9

# ======================================

# PERMUTATION & SHUFFLE
arr1D = [10, 20, 30, 40, 50, 60]
print("\nList Array 1D: \n", arr1D)
arr2D = np.array([[1, 2], [3, 4], [5, 6]])
print("\nList Array 2D: \n", arr2D)

# permutation -> menyalin (copy) data asli lalu di-shuffle dan mengembalikan array baru
# .permutation(array)
arrPermutation1D = np.random.permutation(arr1D)
print("\nHasil dari Permutation 1D:\n", arrPermutation1D)
arrPermutation2D = np.random.permutation(arr2D)
print("\nHasil dari Permutation 2D:\n", arrPermutation2D)

# shuffle -> TIDAK menyalin (not copy) data asli tapi langsung di-shuffle
# .shuffle(array)
np.random.shuffle(arr1D)
print("\nHasil dari Shuffle 1D:\n", arr1D)
np.random.shuffle(arr2D)
print("\nHasil dari Shuffle 2D:\n", arr2D)
