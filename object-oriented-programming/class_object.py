class Kampus:
    pass

kampus1 = Kampus()

print(type(kampus1))

# ======================================

# INSTANCE ATTRIBUTE
class Mahasiswa:
    pass

mahasiswa1 = Mahasiswa()
mahasiswa1.nim = "L200230141"
mahasiswa1.name = "Arya"

print(mahasiswa1.nim)
print(mahasiswa1.name)

# ======================================

# CLASS ATTRIBUTE
class Dosen:
    name = "name example"
    address = "address example"

dosen1 = Dosen()
print(dosen1.name)
print(dosen1.address)

# ======================================

# CLASS WITH METHODS
class Car:
    type = ""
    color = ""

    def run(self):
        print(f"{self.type} car is running")

car1 = Car()
car1.type = "Sport"
car1.run()

# ======================================

# METHODS WITH PARAMETER
class Siswa:
    name = ""
    grade = ""

    def hello(self, name):
        print(f"Halo {name}, nama saya {self.name}")

siswa1 = Siswa()
siswa1.name = "Budi"
siswa1.hello("Ari")