


class Jugador:
    #Contador global
    JUGADORES_CREADOS = 0
    POSICIONES_VALIDAS = {"DEL", "VOL", "DEF", "ARQ"}

    def __init__(self, nombre, edad: int, posicion, club, energia: int, goles: int):
        # Atributos privados
        self.__nombre = nombre
        self.__edad = edad
        self.__posicion = posicion
        self.__goles = 0

        # Atributos publicos
        self.club = club
        self.energia = energia

        assert nombre != "", "La edad debe ser mayor o igual a 15"
        assert edad >= 15, "La edad debe ser mayor o igual a 15"
        assert self.posicion_valida(posicion), "Posicion no valida"
        

        Jugador.JUGADORES_CREADOS += 1



    # Retorna la cantidad de jugadores creados
    @classmethod
    def creados(cls):
        return cls.JUGADORES_CREADOS
    
    # Ve si la poscion es valida
    @staticmethod
    def posicion_valida(validar):
        return validar in ["DEL", "VOL", "DEF", "ARQ"]

    # Retorna el nombre del jugador
    def nombre(self):
        return self.__nombre

    # Rtorna la edad del jugador
    @property
    def edad(self):
        return self.__edad

    # Para añadir una nueva edad
    @edad.setter
    def edad(self, nueva_edad):
        assert nueva_edad >= 15, "La edad debe ser igual o mayor a 15"
        self.__edad = nueva_edad

    # Retorna lo goles del jugador
    def goles(self):
        return self.__goles

    # Para añadir los goles del jugador
    def anotar_gol(self):
        assert self.__goles >= 0, "Debe ser igual o mayor a cero goles"
        self.__goles += 1
        '''assert''' 

    '''def entrenar():
        if self.energia < 0:'''
        

    def __str__(self):
        return f"{self.__nombre}, Club: {self.club}, Posicion: {self.__posicion}, Energia: {self.energia}, Goles: {self.__goles}"




# Creacion de objeto
j1 = ("Pedro", 19, "DEL", "Deportes Castro", 70)
j2 = ("Matias", 21, "DEF", "Deportes Castro", 80)


'''j1.club = "Deportes Castro"
    j1.energia = 70
    j2.club = "Deportes Castro"
    j1.energia = 80'''

'''j1.entrenar(20)
        j1.anotar_gol()
        j2.anotar_gol()'''


print("Los jugadores creados son: ", Jugador.creados())
print f"{j1}, Club: {self.club}, Posicion: {self.__posicion}, Energia: {self.energia}, Goles: {self.__goles}"

