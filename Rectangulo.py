#!/bin/bash
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __eq__(self, other):
        if not isinstance(other, Rectangulo):
            return False
        return self.base == other.base and self.altura == other.altura
    def __lt__(self, other):
      if not isinstance(other, Rectangulo):
        return False
      return self.area() < other.area()
    

rectangulo1 = Rectangulo(4,5)
rectangulo2 = Rectangulo(4,5)

rectangulo3 = Rectangulo(6,7) 
print(f'Rectangulo 1 y 2 iguales: ',rectangulo1 == rectangulo2)
print(f'Rectangulo 1 y 3 iguales: ',rectangulo1 == rectangulo3)
print(f'Rectangulo 1 menor que 2: ',rectangulo1 < rectangulo2)
print(f'Rectangulo 1 menor que 3: ', rectangulo1 < rectangulo3)