# Ejercicio 3 hecho en Clases (Unidad 1)

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    # Suma de 2 fracciones
    def __add__(self, otro):
        num = self.numerador * otro.denominador + otro.numerador * self.denominador
        den = self.denominador * otro.denominador
        return Fraccion(num, den)
    
    # Multiplicacion de 2 fracciones
    def __mul__(self, otro):
        num = self.numerador * otro.numerador
        den = self.denominador * otro.denominador
        return Fraccion(num, den)
    
    def __eq__(self, otro):
        return(self.numerador * otro.denominador ==
               self.denominador * otro.numerador)

f1 = Fraccion(1, 2)
f2 = Fraccion(2, 4)

suma = f1 + f2
multiplicacion = f1 * f2
igualdad = f1 == f2

print("Fraccion 1:", f1)
print("Fraccion 2:", f2)
print(f"La suma de 1/2 y 2/4 es:", suma)
print(f"La multiplicacion de 1/2 y 2/4 es:", multiplicacion)
print(f"¿1 es igual a 2?", igualdad)
