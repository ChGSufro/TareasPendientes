from src.app.Tarea import Tarea
from src.api.Api import get_tareas_event as cargar_tareas

class UsuarioActivo():
# Clase que representa un usuario activo
# params: rut -> str -> rut del usuario
# params: nombre -> str -> nombre del usuario
# Atributos:
    # rut -> str -> rut del usuario
    # nombre -> str -> nombre del usuario
    # tareas -> list -> lista de tareas del usuario con objetos de la clase Tarea

    def __init__(self, rut, nombre):
        self.CH_G_rut = rut
        self.CH_G_nombre = nombre
        self.CH_G_tareas = []
        self.updateTareas()
        print(self.CH_G_tareas)

    # getters de la clase
    def getRut(self):
        return self.CH_G_rut
    
    def getNombre(self):
        return self.CH_G_nombre

    def getTareas(self):
        return self.CH_G_tareas
    
    def getTarea(self, id_tarea):
        for tarea in self.CH_G_tareas:
            if tarea.getId() == id_tarea:
                return tarea
        return None, "La tarea no existe."
    
    # Metodo que actualiza la lista de tareas del usuario con las tareas de la base de datos
    def updateTareas(self):
        self.CH_G_tareas = self.instanciar_tareas(cargar_tareas(self.CH_G_rut)["respuesta"])
    
    # Metodo que verifica si una tarea existe en la lista de tareas del usuario
    # params: id_tarea -> int -> id de la tarea
    # return: bool -> True si la tarea existe, False si no existe
    def mi_tarea_existe(self, id_tarea):
        for tarea in self.CH_G_tareas:
            if tarea.getId() == id_tarea:
                return True
        return False, "La tarea no existe."

    # Metodo que instancia las tareas de un diccionario
    # params: tareas_dict -> list -> lista de diccionarios con las tareas -> [{Id, Nombre, Descripcion, Estado}]
    # return: list -> lista de objetos de la clase Tarea -> [Tarea1, Tarea2, ...]
    def instanciar_tareas(self, tareas_dict):
        CH_G_tareas = []
        for tarea in tareas_dict:
            CH_G_tareas.append(Tarea(tarea["_id"], tarea["Nombre"], tarea["Descripcion"], tarea["Estado"]))
        return CH_G_tareas

