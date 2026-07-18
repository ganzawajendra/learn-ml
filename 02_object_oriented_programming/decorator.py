class Matematika:

    @staticmethod
    def tambah(a, b):
        return a + b

angka1 = Matematika.tambah(3, 4)
print(angka1)

print(Matematika.tambah(10, 10)) # Tidak usah membuat objek

# ======================================

class BankAccount:
    no = ""
    balance = 0
    is_active = True

    def __init__(self, no, balance = 0):

        if(balance < 0):
            raise ValueError("Saldo tidak boleh negatif")
        
        self.no = no
        self.balance = balance
    
    def __str__(self):
        return f"Bank account {self.no} has balance {self.balance} and status {self.is_active}"
    
    @classmethod
    def disabled(cls, no, balance = 0):
        result = cls(no, balance)
        result.is_active = False
        return result

bank1 = BankAccount("1029380", 10000)
bank2 = BankAccount.disabled("2038482", 20000)

print(bank1)
print(bank2)

# ======================================

# PROPERTY METHOD FOR CONTROL ACCESS
class Category:
    _name: "" # Tidak bisa diakses langsung

    @property
    def name(self):
        return self._name
    
    @get_name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Nama tidak boleh kosong")
        self._name = name


category1 = Category()
category1.name = "Fruits"
print(category1.name)
# print(category1.get_name())