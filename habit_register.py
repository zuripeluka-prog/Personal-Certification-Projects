class tarea:
    def __init__(self, id_tarea, titulo, prioridad, etiquetas):
        self.id_tarea = id_tarea
        self.titulo = titulo
        self.prioridad = prioridad
        self.etiquetas = etiquetas
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = 'x' if self.completada else ' '
        etiquetas_str = ', '.join(self.etiquetas)
        return f"[{estado}] ID: {self.id_tarea}, Título: {self.titulo}, Prioridad: {self.prioridad}, Etiquetas: {etiquetas_str}"

class gestor_tareas:
    def __init__(self):
        self.tareas = {}
        self.todas_las_etiquetas = set()
        self.count_id = 1

    def agregar_tarea(self, titulo, prioridad, etiquetas):
        id_tarea = self.count_id
        nueva_tarea = tarea(id_tarea, titulo, prioridad, etiquetas)
        self.tareas[id_tarea] = nueva_tarea
        self.todas_las_etiquetas.update(etiquetas)
        self.count_id += 1
        print(f"Tarea agregada: {nueva_tarea}")

    def completar_tarea(self, id_tarea):
        if id_tarea in self.tareas:
            self.tareas[id_tarea].marcar_completada()
            return True
        else:
            return False

    def mostrar_tareas(self):
        for tarea in self.tareas.values():
            print(tarea)

    def mostrar_todas_las_etiquetas(self):
        print("Etiquetas disponibles:")
        for etiqueta in self.todas_las_etiquetas:
            print(f"- {etiqueta}")

    
gestor = gestor_tareas()
while True:
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Mostrar tareas")
    print("4. Mostrar todas las etiquetas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Ingrese el título de la tarea: ")
        prioridad = input("Ingrese la prioridad de la tarea (alta, media, baja): ")
        etiquetas = input("Ingrese las etiquetas separadas por comas: ").split(",")
        etiquetas = [etiqueta.strip() for etiqueta in etiquetas]
        id_tarea = gestor.agregar_tarea(titulo, prioridad, etiquetas)
        print(f"Tarea agregada con ID: {id_tarea}")

    elif opcion == "2":
        id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
        if gestor.completar_tarea(id_tarea):
            print(f"Tarea con ID {id_tarea} marcada como completada.")
        else:
            print(f"No se encontró una tarea con ID {id_tarea}.")

    elif opcion == "3":
        gestor.mostrar_tareas()

    elif opcion == "4":
        gestor.mostrar_todas_las_etiquetas()

    elif opcion == "5":
        print("Saliendo del gestor de tareas.")
        break

    else:
        print("Opción no válida. Por favor, intente nuevamente.")