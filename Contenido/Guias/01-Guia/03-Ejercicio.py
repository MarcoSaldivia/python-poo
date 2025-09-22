# Ejercico 3 - Guia de Estudio N1

class Producto:
    def __init__(self, nombre, precio, cantidad, codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
        self.historial = []  

    # Método para actualizar stock
    def actualizar_stock(self, cantidad_cambio):
        self.cantidad += cantidad_cambio
        self.historial.append(cantidad_cambio)

    # Método para calcular valor total de este producto
    def valor_total(self):
        return self.precio * self.cantidad

    # Método mágico para mostrar información del producto
    def __str__(self):
        return f"Producto: {self.nombre}, Código: {self.codigo}, Precio: ${self.precio}, Cantidad: {self.cantidad}, Historial: {self.historial}"



class Inventario:
    def __init__(self):
        self.productos = {} 

    # Agregar nuevo producto
    def agregar_producto(self, producto):
        self.productos[producto.codigo] = producto

    # Actualizar stock de un producto existente
    def actualizar_producto(self, codigo, cantidad_cambio):
        if codigo in self.productos:
            self.productos[codigo].actualizar_stock(cantidad_cambio)
        else:
            print("Producto no encontrado en el inventario.")

    # Mostrar todos los productos
    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    # Calcular valor total del inventario
    def valor_total_inventario(self):
        total = sum(p.valor_total() for p in self.productos.values())
        return total


# EJEMPLO 

p1 = Producto("Manzanas", 1000, 50, "A001")
p2 = Producto("Peras", 1200, 30, "P001")

# Crear inventario y agregar productos
inventario = Inventario()
inventario.agregar_producto(p1)
inventario.agregar_producto(p2)

# Mostrar productos
inventario.mostrar_productos()

# Actualizar stock
inventario.actualizar_producto("A001", 20)  # Se suman 20 manzanas
inventario.actualizar_producto("P001", -5)  # Se venden 5 peras

# Mostrar productos después de actualizar stock
print("Después de actualizar stock:")
inventario.mostrar_productos()

# Valor total del inventario
print("Valor total del inventario: $", inventario.valor_total_inventario())
