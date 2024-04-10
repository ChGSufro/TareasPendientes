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
        return {"_id": self.CH_G_id, "Nombre": self.CH_G_nombre, "Descripcion": self.CH_Gdescripcion, "Estado": self.CH_Gestado}
    
    def nombre_valido(self, nombre):
        if nombre == self.CH_G_nombre:
            raise ValueError("El nombre no puede ser igual al actual")
        nombre.replace(" ", "")
        if nombre == "":
            return False
        return True
    
    def descripcion_valida(self, descripcion):
        if descripcion == self.CH_Gdescripcion:
            raise ValueError("La descripcion no puede ser igual a la actual")
        descripcion.replace(" ", "")
        if descripcion == "":
            return False
        return True
    
    def estado_valido(self, estado):
        if estado == self.CH_Gestado:
            False
        if estado != "Pendiente" and estado != "En Proceso" and estado != "Finalizada":
            return False
        return True
    
    def modificar_tarea(self, nombre, descripcion, estado):
        if self.nombre_valido(nombre):
            self.setNombre(nombre)
        if self.descripcion_valida(descripcion):
            self.setDescripcion(descripcion)
        if self.estado_valido(estado):
            self.setEstado(estado)

    