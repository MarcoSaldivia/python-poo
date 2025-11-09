import random

class Vehiculo:
    def __init__(self, marca, año, color):
        self.marca = marca
        self.año = año
        self.color = color

    def moverse(self):
        pass


class Terrestre(Vehiculo):
    def rodar(self):
        print("Rodando sobre ruedas por el asfalto")


class Acuatico(Vehiculo):
    def navegar(self):
        print("Navegando sobre el agua")


class Aereo(Vehiculo):
    def volar(self):
        print("Volando por el aire")


class VehiculoAnfibio(Terrestre, Acuatico):
    def moverse(self):
        self.rodar()
        self.navegar()


class Hidroavion(Acuatico, Aereo):
    def moverse(self):
        self.navegar()
        self.volar()


# Terrestres
class Coche(Terrestre):
    def moverse(self):
        self.rodar()

class Moto(Terrestre):
    def moverse(self):
        self.rodar()

class Camion(Terrestre):
    def moverse(self):
        self.rodar()


# Acuáticos
class Lancha(Acuatico):
    def moverse(self):
        self.navegar()

class Bote(Acuatico):
    def moverse(self):
        self.navegar()

class Yate(Acuatico):
    def moverse(self):
        self.navegar()


# Aéreos
class Avion(Aereo):
    def moverse(self):
        self.volar()

class Helicoptero(Aereo):
    def moverse(self):
        self.volar()

class Dron(Aereo):
    def moverse(self):
        self.volar()


# Híbridos
class AnfibioPequeno(VehiculoAnfibio):
    pass

class HidroavionComercial(Hidroavion):
    pass

class HidroavionMilitar(Hidroavion):
    pass


def simular_carrera():
    terrestres = [
        Coche("Toyota Corolla", 2020, "Rojo"),
        Moto("Yamaha FZ", 2022, "Negro"),
        Camion("Volvo FH", 2019, "Blanco")
    ]

    acuaticos = [
        Lancha("Sea Ray 230", 2021, "Azul"),
        Bote("Quicksilver 310", 2020, "Gris"),
        Yate("Sunseeker 76", 2023, "Blanco")
    ]

    aereos = [
        Avion("Boeing 737", 2018, "Blanco"),
        Helicoptero("Bell 206", 2021, "Gris"),
        Dron("DJI Phantom", 2024, "Negro")
    ]

    hibridos = [
        VehiculoAnfibio("Gibbs Aquada", 2019, "Verde"),
        HidroavionComercial("De Havilland Canada", 2020, "Blanco"),
        HidroavionMilitar("Beriev Be-200", 2022, "Gris")
    ]

    vehiculos = terrestres + acuaticos + aereos + hibridos
    random.shuffle(vehiculos)


simular_carrera()
