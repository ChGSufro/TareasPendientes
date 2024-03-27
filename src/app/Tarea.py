class Tarea():
# Clase que representa una tarea
# params: id -> int -> id de la tarea
# params: nombre -> str -> nombre de la tarea
# params: descripcion -> str -> descripcion de la tarea
# params: estado -> str -> estado de la tarea (Pendiente, En Proceso, Finalizada)
# Atributos:
    # id -> int -> id de la tarea
    # nombre -> str -> nombre de la tarea
    # descripcion -> str -> descripcion de la tarea
    # estado -> str -> estado de la tarea (Pendiente, En Proceso, Finalizada)

    def __init__(self, id : int, nombre : str, descripcion : str, estado : str):
        self.CH_G_id = id
        self.CH_G_nombre = nombre
        self.CH_Gdescripcion = descripcion
        self.CH_Gestado = estado

    # Metodos get y set excepto setId
    def getId(self):
        return self.CH_G_id
    
    def getNombre(self):
        return self.CH_G_nombre
    
    def getDescripcion(self):
        return self.CH_Gdescripcion
    
    def getEstado(self):
        return self.CH_Gestado
    
    def setNombre(self, nombre):
        self.CH_G_nombre = nombre
    
    def setDescripcion(self, descripcion):
        self.CH_Gdescripcion = descripcion
    
    def setEstado(self, estado):
        self.CH_Gestado = estado

    # Metodo que convierte la tarea en un diccionario
    # return: dict -> {Id, Nombre, Descripcion, Estado}
    def to_dict(self):
        return {"Id": self.CH_G_id, "Nombre": self.CH_G_nombre, "Descripcion": self.CH_Gdescripcion, "Estado": self.CH_Gestado}

    