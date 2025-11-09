
class Animal:
    def __init__(self, nombre, edad, peso, genero):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.genero = genero

def comer(self):
    print(f"{self.nombre} esta comiendo")

def dormir(self):
    print(f"{self.nombre} esta durmiendo")

def mostrar_ficha(self):
    print(f"Nombre: {self.nombre}")
    print(f"Edad: {self.edad} años")
    print(f"Peso: {self.peso} kg")
    print(f"Genero: {self.genero}")




class Perro(Animal):
    def __init__(self, nombre, edad, peso, genero, raza):
        super().__init__(nombre, edad, peso, genero)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} esta ladrando")


    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Genero: {self.genero}")
        print(f"Raza: {self.raza}")




class Gato(Animal):
    def __init__(self, nombre, edad, peso, genero, color_pelaje):
        super().__init__(nombre, edad, peso, genero)
        self.color_pelaje = color_pelaje

    def maullar(self):
        print(f"{self.nombre} esta maullando")


    def mostra_ficha(self):
        super().mostrar_ficha()
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Genero: {self.genero}")
        print(f"Color de pelaje: {self.color_pelaje}")




class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, genero, color_plumaje):
        super().__init__(nombre, edad, peso, genero)
        self.color_plumaje = color_plumaje

    def volar(self):
        print(f"{self.nombre} esta volando")


    def mostra_ficha(self):
        super().mostrar_ficha()
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Genero: {self.genero}")
        print(f"Color de plumaje: {self.color_plumaje}")






perro1 = Perro("Rocky", 3, 20, "Macho", "Labrador")
gato1 = Gato("Mishi", 2, 4, "Hembra", "Blanco con negro")
pajaro1 = Pajaro("Coco", 1, 0.5, "Macho", "Amarillo")


perro1.mostrar_ficha()
perro1.ladrar()

gato1.mostrar_ficha()
gato1.maullar()

pajaro1.mostrar_ficha()
pajaro1.volar()



