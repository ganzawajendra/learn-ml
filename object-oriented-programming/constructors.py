class Mahasiswa:
    name = ""
    nim = ""

    def __init__(self, name, nim):
        self.name = name
        self.nim = nim

mahasiswa1 = Mahasiswa("Budi", "L200230141")
print(mahasiswa1.name)
print(mahasiswa1.nim)

# ======================================

# CONSTRUCTORS WITH CHECK
class BankAccount:
    no = ""
    saldo = 0

    def __init__(self, no, saldo):

        if(saldo < 0):
            raise ValueError("Saldo tidak boleh negatif")

        self.no = no
        self.saldo = saldo

bank1 = BankAccount("1230819", 10000)
print(bank1.no)
print(bank1.saldo)

# bank2 = BankAccount("1230813", -10000)
# print(bank2.no)
# print(bank2.saldo)

# ======================================

# OTHER SPECIAL METHODS
class Dosen:
    name = ""
    address = ""

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Hai nama saya {self.name} dan saya tinggal di {self.address}"
    
    def __eq__(self, other):
        return self.name == other.name and self.address == other.address

    # __lt__(self, other) -> kurang dari <
    # __gt__(self, other) -> lebih dari >
    # __le__(self, other) -> kurang dari sama dengan <=
    # __ge__(self, other) -> lebih dari sama dengan >=

dosen1 = Dosen("Ari", "Jl. Budi Utomo")
dosen2 = Dosen("Ari", "Jl. Budi Utomo")
dosen3 = Dosen("Budi", "Jl. Jend. Sudirman")

print(dosen1) # __str__
print(dosen1 == dosen2) # __eq__
print(dosen1 == dosen3) # __eq__

