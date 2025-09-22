# Ejercico 4 - Guia de Estudio N1


class Pedido:
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.platos = []  # Lista de tuplas: (nombre, precio)
        self.total = 0

    # Método para añadir un plato
    def agregar_plato(self, nombre, precio):
        self.platos.append((nombre, precio))
        self.calcular_total()

    # Método para calcular total
    def calcular_total(self):
        self.total = sum(precio for _, precio in self.platos)

    # Método mágico para contar platos
    def __len__(self):
        return len(self.platos)

    # Método mágico para combinar pedidos de la misma mesa
    def __add__(self, otro):
        if self.numero_mesa != otro.numero_mesa:
            print("No se pueden combinar pedidos de mesas diferentes.")
            return None
        nuevo_pedido = Pedido(self.numero_mesa)
        nuevo_pedido.platos = self.platos + otro.platos
        nuevo_pedido.calcular_total()
        return nuevo_pedido

    # Finalizador
    def __del__(self):
        print(f"Pedido de la mesa {self.numero_mesa} completado.")

    # Mostrar información del pedido
    def __str__(self):
        detalles = ', '.join([f"{nombre} (${precio})" for nombre, precio in self.platos])
        return f"Mesa {self.numero_mesa}: {detalles}. Total: ${self.total}"


# EJEMPLO
pedido1 = Pedido(5)
pedido1.agregar_plato("Hamburguesa", 5000)
pedido1.agregar_plato("Refresco", 1500)

pedido2 = Pedido(5)
pedido2.agregar_plato("Papas Fritas", 2000)

print(pedido1)
print("Número de platos en pedido1:", len(pedido1))

# Combinar pedidos
pedido_combinado = pedido1 + pedido2
print("Pedido combinado:")
print(pedido_combinado)

# Eliminar un pedido
del pedido1
