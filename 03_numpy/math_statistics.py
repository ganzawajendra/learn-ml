import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# 2D array
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# 3D array
arr3 = np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]], [[5, 5, 5], [6, 6, 6]]])

# ======================================

# MEAN
# .mean(array, axis, dtype, keepdims)
# axis = 0 -> menghitung rata-rata ke bawah
# axis = 1 -> menghitung rata-rata ke samping
# keepdims -> True jika ingin mempertahankan dimensi array (array 2D akan ber-output 2D)

mean1 = np.mean(arr1)
mean2 = np.mean(arr2)
mean3 = np.mean(arr2, axis=0)
mean4 = np.mean(arr3)
print(f"Mean dari array 1D: {mean1}")
print(f"Mean dari array 2D: {mean2}")
print(f"Mean array 2D per kolom 2D axis 0: {mean3}")
print(f"Mean dari array 3D: {mean4}")

# ======================================

# MEDIAN
# .median(array, axis, keepdims)

median1 = np.median(arr1)
median2 = np.median(arr2)
median3 = np.median(arr2, axis=0)
median4 = np.median(arr3)
print(f"Median dari array 1D: {median1}")
print(f"Median dari array 2D: {median2}")
print(f"Median array 2D per kolom 2D axis 0: {median3}")
print(f"Median dari array 3D: {median4}")

# ======================================

# VARIANCE
# KUNCI: Rata-rata dari setiap (JARAK DATA KE MEAN) yang dipangkatkan 2.
# TUJUAN: Menghilangkan minus (-) pada jarak data agar tidak saling menghapus.
# EFEK SAMPING: Satuannya jadi ikut kuadrat (misal: cm menjadi cm²).

# .var(array, axis, keepdims)
var1 = np.var(arr1)
var2 = np.var(arr2)
var3 = np.var(arr2, axis=0)
var4 = np.var(arr3)
print(f"Variance dari array 1D: {var1}")
print(f"Variance dari array 2D: {var2}")
print(f"Variance array 2D per kolom 2D axis 0: {var3}")
print(f"Variance dari array 3D: {var4}")

# ======================================

# STANDAR DEVIASI
# KUNCI: Akar kuadrat dari nilai Variance (np.sqrt(np.var(data))).
# TUJUAN: Menjinakkan pangkat 2 dari Variance agar satuannya normal kembali (cm² jadi cm lagi).
# ARTI SKOR: Indeks kekompakan data. Semakin kecil nilainya = data semakin kompak/konsisten.

# .std(array, axis, dtype, keepdims)
# .std() itu sama dengan np.sqrt(np.var(data))

std1 = arr1.std()
std2 = arr2.std()
std3 = arr2.std(axis=0)
std4 = arr3.std()
print(f"Standar Deviasi dari array 1D: {std1}")
print(f"Standar Deviasi dari array 2D: {std2}")
print(f"Standar Deviasi array 2D per kolom 2D axis 0: {std3}")
print(f"Standar Deviasi dari array 3D: {std4}")


# ======================================

# PEEK-TO-PEEK
# TUJUAN: Menghitung nilai puncak ke puncak (nilai terbesar - nilai terkecil)

# .ptp(array, axis, keepdims)
ptp1 = np.ptp(arr1)
ptp2 = np.ptp(arr2)
ptp3 = np.ptp(arr2, axis=0)
ptp4 = np.ptp(arr3)
print(f"Peek to Peek dari array 1D: {ptp1}")
print(f"Peek to Peek dari array 2D: {ptp2}")
print(f"Peek to Peek array 2D per kolom 2D axis 0: {ptp3}")
print(f"Peek to Peek dari array 3D: {ptp4}")

