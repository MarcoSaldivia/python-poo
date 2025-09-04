# 2do ejemplo hecho en clases, en Python.

class Automovil():
    # Constructor de la clase Automovil
    # Atributos de la clase Automovil (caracteristicas compatidas por todos los objetos de la clase)
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

# Metodos de la clase Automovil (Comportamientos)
    def arrancar(self):
        print(f"El {self.marca} {self.modelo}esta arrancando")
        
    def frenar(self):
        print(f"El {self.marca} {self.modelo} esta frenando")

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} esta acelereando")

# Creando un objeto de la clase Automovil
auto1 = Automovil("Toyota", "Corolla", 2020, "Rojo")
auto2 = Automovil("Ford", "Mustang", 2021, "Azul")
auto3 = Automovil("Honda", "civic", 2019, "Negro")

print(f"El auto 1 es un {auto1.marca} {auto1.modelo}")