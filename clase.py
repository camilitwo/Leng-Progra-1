class Rectangulo:
    rectangulos = 0
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        self.__class__.rectangulos = self.__class__.rectangulos + 1
    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)

    def __str__(self):
        return "Rectangulo de largo {} y ancho {}".format(self.largo, self.ancho)
    
class Cuadrado:
    cuadrados = 0
    def __init__(self, lado):
        self.lado = lado
        self.__class__.cuadrados = self.__class__.cuadrados + 1
    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado
    
    def __str__(self):
        return "Cuadrado de lado {}".format(self.lado)
    
class Figuras:
    def __init__(self, lista):
        self.lista = [lista]
    def area(self):
        return sum([i.area() for i in self.lista])
    def perimetro(self):
        return sum([i.perimetro() for i in self.lista])
    def __str__(self):
        return "Figuras: {}".format(self.lista)    
    
    def __add__(self, other):
        return self.lista + other.lista
    

    

x = Rectangulo(3, 6)
y = Rectangulo(11, 22)
z = Cuadrado(11)

a = Figuras([x, y, z])

lista = []

lista.append(x)
lista.append(y)
lista.append(z)

for i in lista:
    print(i)
    print(i.area())
    print(i.perimetro())

print(a)
