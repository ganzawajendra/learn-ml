# Public Attribute
# Protected Attribute -> single underscore (_)
# Private Attribut -> double underscore (__)

class BankAccount:
    __no = ""
    __balance = 0

    def __init__(self, no):
        self.__no = no

    @property
    def balance(self):
        return self.__balance

    @property
    def no(self):
        return self.__no
    
    def topup(self, amount):
        self.__balance += amount
    
    def cashout(self, amount):
        if (self.__balance < amount):
            raise ValueError("Saldo tidak mencukupi")
        self.__balance -= amount
    
    def __str__(self):
        return f"Akun bank {self.__no} dengan saldo {self.__balance}"

bank1 = BankAccount("L202030141")
print(bank1.no)

bank1.topup(1000000)
print(bank1.balance)
print(bank1)

# bank1.cashout(1300000) # error -> Saldo tidak mencukupi
bank1.cashout(300000)
print(bank1.balance)
print(bank1)