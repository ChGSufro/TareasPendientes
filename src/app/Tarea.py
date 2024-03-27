class Tarea():
# Clase que representa una tarea
# Atributos:
# id -> int -> id de la tarea
# nombre -> str -> nombre de la tarea
# descripcion -> str -> descripcion de la tarea
# estado -> str -> estado de la tarea (Pendiente, En Proceso, Finalizada)

    def __init__(self, id : int, nombre : str, descripcion : str, estado : str):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    # Metodos get y set excepto setId
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion
    
    def getEstado(self):
        return self.estado
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def setEstado(self, estado):
        self.estado = estado

    # Metodo que convierte la tarea en un diccionario
    # return: dict -> {Id, Nombre, Descripcion, Estado}
    def to_dict(self):
        return {"Id": self.id, "Nombre": self.nombre, "Descripcion": self.descripcion, "Estado": self.estado}

    