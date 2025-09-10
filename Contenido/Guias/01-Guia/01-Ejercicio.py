# Ejercico 1 - Guia de Estudio N1

class ReservaHostal:
    def __init__(self, nombre_cliente, fecha_entrada, fecha_salida, numero_habitacion):
        self.nombre_cliente = nombre_cliente
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.numero_habitacion = numero_habitacion

    def calcular_duracion(self):
        return int(self.fecha_salida) - int(self.fecha_entrada)

    def cambiar_fecha_salida(self, nueva_fecha_salida):
        self.fecha_salida = nueva_fecha_salida
        print(f"La nueva fecha de salida es {self.fecha_salida}")

    def __str__(self):
        return (f"Reserva de {self.nombre_cliente} | Habitación: {self.numero_habitacion}"
                f"Entrada: {self.fecha_entrada} - Salida: {self.fecha_salida}"
                f"Duración: {self.calcular_duracion()} noches")

    def __del__(self):
        print(f"La reserva de {self.nombre_cliente} ha sido cancelada.")


# Ejemplo 
reserva1 = ReservaHostal("Ana López", "15", "20", 5)

print(reserva1) 
print("Duración:", reserva1.calcular_duracion(), "noches")

# Cambiar fecha de salida
reserva1.cambiar_fecha_salida("22")
print(reserva1)

# Eliminar reserva
del reserva1
