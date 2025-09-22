# Laboratorio 1

class Gato:
    def __init__(self, nombre, edad, nvl_energia=100, nvl_hambre=0):
        self.nombre = nombre
        self.edad = edad
        self.nvl_energia = nvl_energia  # 0(min) 100(máx)
        self.nvl_hambre = nvl_hambre    # 0(no hambre) 100(mucha hambre)

    # Metodo jugar
    def jugar(self, duracion):
        self.nvl_enegia -= duracion * 5
        self.nvl_hambre += duracion * 3

        if self.nvl_energia < 0:
            self.nvl_energia = 0
        if self.nvl_hambre > 100:
            self.nvl_hambre = 100

    # Metodo alimentar
    def alimentar(self):
        self.nvl_energia = min(100, self.nvl_energia + 20)
        self.nvl_hambre = max(0, self.nvl_hambre - 20)
        print(f"El gato {self.nombre} ha sido alimentado, su nivel de energía es: {self.nvl_energia} y su nivel de hambre es: {self.nvl_hambre}")


class Espacio:
    def __init__(self, nom_espacio, capacidad_max):
        self.nom_espacio = nom_espacio
        self.capacidad_max = capacidad_max
        self.gatos_presentes = []





    # Metodo para eliminar
    del Gato1 
    print(f"El gato {Gato1.nombre} a salido del Cafe")


# Creacion de Objetos
Gato1 = Gato("Michi", 1, 70, 80)
Gato2 = Gato("Lucas", 3, 100, 60)
Gato3 = Gato("Hector", 2, 50, 70)

print(f"El nombre del primer gato es. {Gato1.nombre}")
print(f"El nombre del segundo gato es :{Gato2.nombre}")
print(f"El nombre del tercer gato es: {Gato3.nombre}")

print(f"La edad de Michi es: {Gato1.edad}")
print(f"La edad de Lucas es: {Gato2.edad}")
print(f"La edad de Hector es: {Gato3.edad}")

print(f"El nivel de energia de Michi es: {Gato1.nvl_energia}")
print(f"El nivel de energia de Lucas es: {Gato2.nvl_energia}")
print(f"El nivel de energia de Hector es: {Gato3.nvl_energia}")

print(f"El nivel de hambre de Michi es: {Gato1.nvl_hambre}")
print(f"El nivel de hambre de Lucas es: {Gato2.nvl_hambre}")
print(f"El nivel de hambre de Hector es: {Gato3.nvl_hambre}")


































#lista gato vacia