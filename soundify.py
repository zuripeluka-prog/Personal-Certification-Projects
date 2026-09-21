
class cancion:
    def __init__(self, titulo, artista, duracion, generos):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.generos = generos

    def obtener_formato_tiempo(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f'{minutos}:{segundos}'

class playlist:
    def __init__(self):
        self.canciones = []
        self.todos_los_generos = set()

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        self.todos_los_generos.update(cancion.generos)

    def duracion_total(self):
        total_duracion = sum(cancion.duracion for cancion in self.canciones)
        return total_duracion

    def mostrar_canciones(self):
        for cancion in self.canciones:
            print(f'Título: {cancion.titulo}, Artista: {cancion.artista}, Duración: {cancion.obtener_formato_tiempo()}, Géneros: {", ".join(cancion.generos)}')

class Soundify:
    def __init__(self):
        self.catologo = {}
        self.playlists = {}
        self.artistas_unicos = set()
        self.generos_unicos = set()

    def subir_cancion(self, cancion):
        self.catologo[cancion.titulo] = cancion
        self.artistas_unicos.add(cancion.artista)
        self.generos_unicos.update(cancion.generos)

    def crear_playlist(self, nombre_playlist, canciones):
        nueva_playlist = playlist()
        for cancion in canciones:
            nueva_playlist.agregar_cancion(cancion)
        self.playlists[nombre_playlist] = nueva_playlist

    def reproducir_cancion(self, titulo_cancion):
        if titulo_cancion in self.catologo:
            cancion = self.catologo[titulo_cancion]
            print(f'Reproduciendo: {cancion.titulo} de {cancion.artista}')
        else:
            print('Canción no encontrada en el catálogo.')

    def explorar_por_genero(self, genero):
        canciones_encontradas = [cancion for cancion in self.catologo.values() if genero in cancion.generos]
        if canciones_encontradas:
            print(f'Canciones del género {genero}:')
            for cancion in canciones_encontradas:
                print(f'- {cancion.titulo} de {cancion.artista}')
        else:
            print(f'No se encontraron canciones del género {genero}.')

    def ver_artistas_unicos(self):
        print('Artistas únicos en el catálogo:')
        for artista in self.artistas_unicos:
            print(f'- {artista}')

app = Soundify()
while True:
    print('Bienvenido a Soundify')
    print('1. Subir canción')
    print('2. ver catologo de canciones')
    print('3. explorar por género o artista')
    print('4. crear playlist')
    print('5. agregar canción a playlist')
    print('6. ver mis mis playlists y reproducir canciones')
    print('7. salir')
    try:
        opcion = int(input('Seleccione una opción: '))
    except ValueError:
        print('Opción inválida. Por favor, ingrese un número del 1 al 7.')
        continue

    if opcion == 1:
        titulo = input('Ingrese el título de la canción: ')
        artista = input('Ingrese el nombre del artista: ')
        duracion = int(input('Ingrese la duración de la canción en segundos: '))
        generos = input('Ingrese los géneros de la canción (separados por comas): ').split(',')
        nueva_cancion = cancion(titulo, artista, duracion, generos)
        app.subir_cancion(nueva_cancion)

    elif opcion == 2:
        print('Catálogo de canciones:')
        for titulo, cancion in app.catologo.items():
            print(f'- {titulo} de {cancion.artista}')

    elif opcion == 3:
        criterio = input('Ingrese el género o artista para explorar: ')
        print(app.explorar_por_genero(criterio))
        print(app.ver_artistas_unicos())

    elif opcion == 4:
        nombre_playlist = input('Ingrese el nombre de la nueva playlist: ')
        app.crear_playlist(nombre_playlist, [])

    elif opcion == 5:
        nombre_playlist = input('Ingrese el nombre de la playlist: ')
        titulo_cancion = input('Ingrese el título de la canción a agregar: ')
        if nombre_playlist in app.playlists and titulo_cancion in app.catologo:
            cancion_a_agregar = app.catologo[titulo_cancion]
            app.playlists[nombre_playlist].agregar_cancion(cancion_a_agregar)
            print(f'Canción "{titulo_cancion}" agregada a la playlist "{nombre_playlist}".')

    elif opcion == 6:
        print('Playlists disponibles:')
        if not app.playlists:
            print('No hay playlists creadas.')
        for nombre in app.playlists:
            print(f'- {nombre}')
        nombre_playlist = input('Ingrese el nombre de la playlist que desea ver: ')
        if nombre_playlist in app.playlists:
            playlist_seleccionada = app.playlists[nombre_playlist]
            print(f'Canciones en la playlist "{nombre_playlist}":')
            playlist_seleccionada.mostrar_canciones()
            titulo_cancion = input('Ingrese el título de la canción a reproducir: ')
            app.reproducir_cancion(titulo_cancion)
            print(f'Reproduciendo canción "{titulo_cancion}" de la playlist "{nombre_playlist}".')

    elif opcion == 7:
        print('Saliendo de la aplicación. ¡Hasta luego!')
        break