class Tarea():
    def __init__(self, id : int, nombre : str, descripcion : str, estado : str):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

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

    def to_dict(self, usuario):
        return {
            "Id": self.id,
            "Usuario": usuario,
            "Nombre": self.nombre,
            "Descripcion": self.descripcion,
            "Estado": self.estado
        }