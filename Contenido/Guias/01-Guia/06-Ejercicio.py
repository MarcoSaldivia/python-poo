# Ejercico 6 - Guia de Estudio N1


class Cancion:
    # Constructor
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = int(duracion_segundos)

    # Metodos de Clases

    # Convertir la duracion a Formato
    def milisegundos(self):
        # Corroborar el paso de milisegundos a minutos
        m, s = divmod(max(self.duracion_segundos(), 0), 60)
        return f"{m}:{s}"

    def __str__(self):
        return f"{self.titulo} - {self.artista} {self:duracion_segundos}"



class Playlist:
    # Constructor de Clase
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = [] # Lista del numero de camciones de la playlist

    # Metodos de Clase

    # Agrega cancion a la playlist
    def agregar(self, cancion):
        self.canciones.append(cancion)

    # Duracion total de la playlist
    def duracion_total(self):
        # Iterador for en una Linea
        return sum(c.duracion_segundos for c in self.canciones)
    
    # Muestra la duracion total en milisegundos
    def milisegundos_total(self):
        total = self.duracion_total()
        m, s = divmod(max(total, 0), 60)
        return f"{m}:{s}"
    
    # Contar el numero de canciones
    def __len__(self):
        return  len(self.canciones)
    
    # Convinacion de las dos playlist
    def __add__(self, otra):
        # Se creo una variable que fusiona ambas playlist en una nueva
        nueva = Playlist(f"{self.nombre} + {otra.nombre}")

        # Guardando canciones en la nueva playlist conbinada
        nueva.canciones = self.canciones + otra.canciones
        return nueva
    
    def __str__(self):
        # Encabezado a mostrar de la playlist
        encabezado = f"Playlist: {self.nombre} | {len(self.canciones)} | Total: {self.milisegundos_total()}"
        # Lanzar mensaje si la lista esta vacia
        if not self.canciones:
            return encabezado , f"Lista Vacia"
        
        # para lacreacion del formato de inpresion de la playlist
        lineas = encabezado

        # Creacion de ciclo para mostrar el listado de canciones para la playlist conbinada
        for i , c in enumerate(self.canciones):
            lineas.append(f"{i}: {c}")
            return "\n".join(lineas) # combina el salto de linea
        
    
    # Instanciar Clases (Creacion de Objetos)
        
