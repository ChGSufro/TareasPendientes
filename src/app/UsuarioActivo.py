from src.app.Tarea import Tarea
from src.api.Api import get_tareas_event as cargar_tareas

class UsuarioActivo():
    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre
        self.tareas = self.updateTareas()


    def getRut(self):
        return self.rut
    
    def getNombre(self):
        return self.nombre

    def getTareas(self):
        return self.tareas
    
    def updateTareas(self):
        self.tareas = cargar_tareas(self.rut)

        
    


    def agregarTarea(self, tarea : dict):
        pass

    def modificarTarea(self, tarea : dict):
        pass

    def eliminarTarea(self, id):
        pass
