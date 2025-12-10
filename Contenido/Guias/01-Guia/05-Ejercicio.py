class Libro:
    def __init__(self, titulo, autor, anio, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.anio}) | Cantidad: {self.cantidad}"


class Biblioteca:
    def __init__(self):
        # Diccionario con: clave = título, valor = instancia de Libro
        self.libros = {}

    # Agregar un libro
    def agregar_libro(self, libro):
        self.libros[libro.titulo] = libro

    # Buscar libro por título
    def buscar_libro(self, titulo):
        return self.libros.get(titulo, None)

    # Actualizar cantidad disponible
    def actualizar_cantidad(self, titulo, nueva_cantidad):
        if titulo in self.libros:
            self.libros[titulo].cantidad = nueva_cantidad
            return True
        return False

    # mostrar todos los libros
    def mostrar_todos(self):
        for libro in self.libros.values():
            print(libro)



# Crear libros
lib1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, 5)
lib2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 3)

# Crear biblioteca
biblio = Biblioteca()

# Agregar libros
biblio.agregar_libro(lib1)
biblio.agregar_libro(lib2)

resultado = biblio.buscar_libro("El Principito")
print(resultado)

# Actualizar
biblio.actualizar_cantidad("El Principito", 10)

# Mostrar todos
biblio.mostrar_todos()
