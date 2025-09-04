# 1er ejemplo de clase en Python. (Semestre 2)

class Animal():
    # Constructor de la clase Animal
    # Atributos de la clase animal (caracteristicas compatidas por todos los objetos de la clase)
    def __init__(self, nombre, especie, edad):    # Self = Referirse a si mismo
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

# Metodos de la clase animal (Comportamientos)
# SELF permite acceder a lo de arriba
    def correr(self):
        print(f"{self.nombre} esta corriendo")
        
    def dormir(self):
        print(f"{self.nombre} esta durmiendo")

# Creando un objeto de la clase Animal
gatito = Animal("Michi", "Gato", 4) 
perrito = Animal("Firulais", "Perro", 2) 
loro = Animal("Loro Pepito", "Ave", 1) 

# Impresión de los atributos de los objetos
print(f"El nombre del animal es: {gatito.nombre}")
print(f"La especie del animal es: {perrito.nombre}")
print(f"La especie del animal  es: {loro.nombre}")

# LLamada a los metodos de los objetos (id , objeto, comportamiento)
gatito.correr()
perrito.correr()
loro.dormir()

