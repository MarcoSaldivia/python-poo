# Cafe de Gatos con Encapsulacion (lab 1)

class Gato:
    def __init__(self, nombre, edad, id_mascota, nvl_energia=100, nvl_hambre=0):
        self.nombre = nombre         
        self.edad = edad      
        self.__id_mascota = id_mascota 
        self.__nvl_energia = nvl_energia 
        self.__nvl_hambre = nvl_hambre 
        self.__estado_salud = "Saludable"
        self.__historial = []           

    # Metodo jugar (Publico)
    def jugar(self, duracion):
        self.__nvl_energia = max(0, self.__nvl_energia - duracion * 5)
        self.__nvl_hambre = min(100, self.__nvl_hambre + duracion * 3)
        self.__registrar_accion(f"Jugo {duracion} min")
        self.__actualizar_salud()

    # Metodo alimentar (Publico)
    def alimentar(self, cantidad=20):
        self.__nvl_energia = min(100, self.__nvl_energia + cantidad)
        self.__nvl_hambre = max(0, self.__nvl_hambre - cantidad)
        self.__registrar_accion(f"Fue alimentado (+{cantidad})")
        self.__actualizar_salud()

    # Metodo actualizar salud (Privado)
    def __actualizar_salud(self):
        if self.__nvl_energia < 20 or self.__nvl_hambre > 80:
            self.__estado_salud = "En observacion"
        if self.__nvl_energia == 0 or self.__nvl_hambre == 100:
            self.__estado_salud = "Enfermo"
        if self.__nvl_energia > 50 and self.__nvl_hambre < 50:
            self.__estado_salud = "Saludable"

    # Metodo registrr acciones (Privado)
    def __registrar_accion(self, accion):
        self.__historial.append(accion)

    # Metodo mmgico
    def __str__(self):
        return f"Gato {self.nombre}, Edad {self.edad}, Salud: {self.__estado_salud}"


class Espacio:
    def __init__(self, nom_espacio, capacidad_max):
        self.nom_espacio = nom_espacio           
        self.__capacidad_max = capacidad_max   
        self.__gatos_presentes = []           

    def agregar_gato(self, gato):
        if len(self.__gatos_presentes) < self.__capacidad_max:
            self.__gatos_presentes.append(gato)
            print(f"{gato.nombre} ingreso al espacio {self.nom_espacio}")
        else:
            print("¡Capacidad maxima alcanzada!")

    def sacar_gato(self, gato):
        if gato in self.__gatos_presentes:
            self.__gatos_presentes.remove(gato)
            print(f"{gato.nombre} salio del espacio {self.nom_espacio}")

    def __str__(self):
        return f"Espacio {self.nom_espacio}, Capacidad {self.__capacidad_max}"



# Creacion de Objeto

Gato1 = Gato("Michi", 1, "CL001", 70, 80)
Gato2 = Gato("Lucas", 3, "CL002", 100, 60)
Gato3 = Gato("Hector", 2, "CL003", 50, 70)

esp = Espacio("Sala Principal", 2)

esp.agregar_gato(Gato1)
esp.agregar_gato(Gato2)

Gato1.jugar(10)
Gato1.alimentar(15)

print(Gato1)
print(Gato2)

