# PARENT CLASS
class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    @property
    def info(self):
        return f"Kendaraan {self.merk} dibuat pada tahun {self.tahun}"
    
    @property
    def nyalakan(self):
        print(f"{self.info} dinyalakan DARI PARENT")

# ======================================

# CLASS CHILD MOBIL
# ketika ada method dari child yang sama dengan parent
# gunakan super() untuk memanggil yang ada di parent
class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_penumpang):
        super().__init__(merk, tahun) # setting merk dan tahun ke __init__ parent
        self.jumlah_penumpang = jumlah_penumpang

    @property
    def info_roda(self):
        print(f"Mobil {self.info} memiliki roda 4")
    
    @property
    def info_penumpang(self):
        print(f"Mobil {self.info} memiliki jumlah penumpang {self.jumlah_penumpang}")

mobil1 = Mobil("Toyota", 2020, 6)
mobil1.nyalakan
mobil1.info_roda
mobil1.info_penumpang

# ======================================

# CLASS CHILD MOTOR
# ketika ingin mendefinisikan ulang method parent
# gunakan OVERRIDING 
class Motor(Kendaraan):

    @property
    def info_roda(self):
        print(f"Motor {self.info} memiliki roda 2")
    
    @property
    def nyalakan(self):
        print(f"Motor {self.info} dinyalakan DARI CHILD")

motor1 = Motor("Scoopy", 2014)
motor1.nyalakan
motor1.info_roda

# ======================================

# MULTILEVEL INHERITANCE
# "a" punya child "b", "b" punya child "c", "c" punya child "d" -> tidak disarankan terlalu banyak
class Karyawan:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class KaryawanTetap(Karyawan):
    pass

class Manager(KaryawanTetap):
    pass

class VicePresident(Manager):
    pass

# ======================================

# MULTIPLE INHERITANCE
# 1 class dapat memiliki 2 paret (python bisa, java tidak bisa
# tapi kondisi ini sebisa mungkin dihindari karena akan terjadi DIAMOND PROBLEM
class BisaBerenang:
    def berenang(self):
        print("Bisa berenang")

class BisaBerlari:
    def berlari(self):
        print("Bisa berlari")

class Atlit(BisaBerenang, BisaBerlari):
    def __init__(self, name):
        self.name = name

x = Atlit("x")
x.berenang()
x.berlari()

# DIAMOND PROBLEM
class A:
    def method(self):
        print("Method dari A")

class B(A):
    def method(self):
        print("Method dari B")

class C(A):
    def method(self):
        print("Method dari C")

class D(B, C):
    pass

# Method yang dijalankan yaitu B terlebih dahulu karena B ditulis duluan daripada C
# dapat menimbulkan kebingungan
d = D()
d.method()