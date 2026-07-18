from abc import ABC, abstractmethod

# Ability of different classes to respond to the same method name or interface with the their own unique behaviors
# Gabungan antara Overriding dan Inheritance
class Hewan:
    def __init__(self, name):
        self.name = name

    def suara(self):
        return "Hewan bersuara"

# inheritance
class Anjing(Hewan):
    def suara(self):
        return f"{self.name} Guk guk!"

# inheritance
class Kucing(Hewan):
    def suara(self):
        return f"{self.name} Meow meow!"

# inheritance
class Sapi(Hewan):
    def suara(self):
        return f"{self.name} Mooo!"

# Polymorphism in action
hewan_list = [
    Anjing("Helly"),
    Kucing("Wiskas"),
    Sapi("Akmal")
]

# Methos dama tapi behaviornya berbeda
for hewan in hewan_list:
    print(hewan.suara())

# ======================================

# DUCK TYPING
# tidak peduli apa class nya, yang penting memiliki method yang sama
# tidak inheritance
class Mobil:
    def start(self):
        return "mesin mobil menyala"

class Motor:
    def start(self):
        return "mesin motor menyala"

class Perahu:
    def start(self):
        return "mesin perahu menyala"

# function yang polymorphic
def operasikan_kendaraan(kendaraan):
    print(kendaraan.start())

# Polymorphism with duck typing
kendaraan_list = [
    Mobil(),
    Motor(),
    Perahu()
]

for kendaraan in kendaraan_list:
    operasikan_kendaraan(kendaraan)

# ======================================

# POLYMORPHISM DENGAN INTERFACE
# python tidak mendukung abstract method (tidak seperti java)
# tapi bisa menggunakan ABS (Abstract Base Class)
# child wajib meng-override method yang abstrak
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

shape_list = [
    Rectangle(3, 4),
    Square(5)
]

for shape in shape_list:
    print(shape.area())