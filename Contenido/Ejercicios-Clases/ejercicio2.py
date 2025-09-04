# Ejercicio 2 hecho en Clases (Unidad 1)

class Coche:
    def __init__(self, marca, gasolina):
        self.marca = marca
        self.gasolina = float(gasolina)
        self.kilometros_recorridos = 0

    def conducir(self, km):
        litros_necesarios = km / 10
        if litros_necesarios <= self.gasolina:
            self.kilometros_recorridos += km
            self.gasolina -= litros_necesarios
            print(f"{self.marca}: Conduciste {km} km. Gasolina restante: {self.gasolina} L")
        else:
            km_posibles = self.gasolina * 10
            self.kilometros_recorridos += km_posibles
            self.gasolina = 0
            print(f"{self.marca}: Solo pudiste conducir {km_posibles} km. Te quedaste sin gasolina.")

    def cargar_gasolina(self, litros):
        self.gasolina += float(litros)
        print(f"{self.marca}: Cargaste {litros} L. Gasolina actual: {self.gasolina} L")


# Crear coches
coche1 = Coche("Toyota", 20)
coche2 = Coche("Ford", 15)

# Usar métodos
coche1.conducir(50)
coche1.cargar_gasolina(10)
coche2.conducir(200)




