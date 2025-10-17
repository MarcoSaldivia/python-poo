
class Playlist:
    total_playlists = 0

    def __init__(self, usuario: str):
        self.usuario = usuario      # publico  
        self._canciones = []        # privdo

        Playlist.total_playlists +=1

    # Agrega 1 cancion a la playlist
    def agregar_cancion(self, nombre_cancion: str) -> None:
        if nombre_cancion and nombre_cancion not in self._canciones:
            self._canciones.append(nombre_cancion)

    # Elimina 1 cancion de la playlist (solo si existe)
    def eliminar_cancion(self, nombre_cancion: str) -> None:
        if nombre_cancion in self._canciones:
            self._canciones.remove(nombre_cancion)
    
    # Retorna la cantidad de cancions en la playlist
    def __len__(self) -> int:
        return len(self._canciones)
    

    def __str__(self) -> str:
        return f"Playlist de {self.usuario} : {self._canciones} canciones"









