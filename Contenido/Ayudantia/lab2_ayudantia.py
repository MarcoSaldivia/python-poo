# 2da Evaluacion Ayudantia POO - Marco Saldivia Mansilla


class Trabajador:
    def __init__(self, nombre):
        self.nombre = nombre

    def tarea(self):
        return f"{self.nombre} realiza tareas generales en el restaurant."



class Chef(Trabajador):
    def __init__(self, nombre, especialidad):
        Trabajador.__init__(self, nombre)
        self.especialidad = especialidad

    def tarea(self):
        return f"El chef {self.nombre} prepara platos de {self.especialidad}."
        


class Mesero(Trabajador):
    def __init__(self, nombre, seccion):
        Trabajador.__init__(self, nombre)  
        self.seccion = seccion

    def tarea(self):
        return f"El mesero {self.nombre} atiende la seccion {self.seccion}."



class AyudanteChefMesero(Chef, Mesero):
    def __init__(self, nombre, especialidad, seccion):
        Chef.__init__(self, nombre, especialidad) 
        Mesero.__init__(self, nombre, seccion)

    def tarea(self):
        return f"El ayudante {self.nombre} prepara los platos de {self.especialidad} y ademas atiene la seccion {self.seccion}"
    


def mostrar_tarea(trabajador):
    print(trabajador.tarea())



chef1 = Chef("Marco", "Empanadas")
mesero1 = Mesero("Matias", "Terraza")
ayudante1 = AyudanteChefMesero("Sofia", "Postres", "Sala Principal")

mostrar_tarea(chef1)
mostrar_tarea(mesero1)
mostrar_tarea(ayudante1)
