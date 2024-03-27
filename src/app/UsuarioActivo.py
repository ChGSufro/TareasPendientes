from src.app.Tarea import Tarea
from src.api.Api import get_tareas_event as cargar_tareas

class UsuarioActivo():
    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre
        self.tareas = []
        self.updateTareas()
        print(self.tareas)


    def getRut(self):
        return self.rut
    
    def getNombre(self):
        return self.nombre

    def getTareas(self):
        return self.tareas
    
    def updateTareas(self):
        self.tareas = self.instanciar_tareas(cargar_tareas(self.rut)["respuesta"])
    
    def mi_tarea_existe(self, id_tarea):
        for tarea in self.tareas:
            if tarea.getId() == id_tarea:
                return True
        return False, "La tarea no existe."

    def instanciar_tareas(self, tareas_dict):
        tareas = []
        for tarea in tareas_dict:
            tareas.append(Tarea(tarea["Id"], tarea["Nombre"], tarea["Descripcion"], tarea["Estado"]))
        return tareas

