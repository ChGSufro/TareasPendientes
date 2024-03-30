import requests

url = "http://44.209.21.223:8081"

# la llave para acceder al return de la api es: "respuesta"
# todos los metodos retornan un json con la llave "respuesta" y un string "Error al comunicar con el servidor." si no se puede conectar con la api.

# metodo de respuesta GET que recibe un rut y devuelve un json con las tareas asociadas a ese id
# params: rut -> str -> rut del usuario
# return: dict -> {Id, Usuario, Nombre, Descripcion, Estado}
def get_tareas_event(rut):
    try:
        CH_Gresponse = requests.get(f"{url}/tareas/get/{rut}")
        return CH_Gresponse.json()
    except requests.exceptions.RequestException:
        return {"respuesta": "Error al comunicar con el servidor."}

# metodo de respuesta POST que recibe un json con una tarea y lo envia para agregalo a la api.
# params: tarea -> dict -> {Usuario, Nombre, Descripcion, Estado}
# retorna un json con un string de confirmacion
def post_tareas_event(tarea):
    try:
        CH_Gresponse = requests.post(f"{url}/tareas/add", json=tarea)
        return CH_Gresponse.json()
    except requests.exceptions.RequestException:
        return {"respuesta": "Error al comnicar con el servidor."}

# metodo de respuesta PUT que recibe un json con una tarea y lo actualiza en la api, retorna un json con un string de confirmacion
# params: tarea -> dict -> {_id, Usuario, Nombre, Descripcion, Estado}
# return: dict -> {respuesta: "Tarea modificada." o "Tarea no encontrada."}
def put_tareas_event(tarea):
    try:
        CH_Gresponse = requests.put(f"{url}/tareas/update", json=tarea)
        return CH_Gresponse.json()
    except requests.exceptions.RequestException:
        return {"respuesta": "Error al comunicar con el servidor."}

# metodo de respuesta DELETE que recibe un id y elimina la tarea asociada a ese id, retorna un json con un string de confirmacion
# params: id -> int -> id de la tarea a eliminar
# return: dict -> {respuesta: "Tarea eliminada." o "Tarea no encontrada."}
def delete_tareas_event(id):
    try:
        CH_Gresponse = requests.delete(f"{url}/tareas/delete/{id}")
        return CH_Gresponse.json()
    except requests.exceptions.RequestException: 
        return {"respuesta": "Error al comunicar con el servidor."}

# metodo de respuesta POST que recibe un json con un usuario y lo envia a la api, retorna un json con el usuario logeado "formato json" si existe o un string si no existe
# params: usuario -> dict -> {_id, Contraseña} -> "_id es el rut"
# return: dict -> {respuesta: {_id, Nombre} o "Usuario y/o contraseña incorrectos"}
def log_usuario_event(CH_Gusuario: dict):
    try:
        CG_Gresponse = requests.post(f"{url}/usuarios/log", json=CH_Gusuario)
        return CG_Gresponse.json()
    except requests.exceptions.RequestException:
        return {"respuesta": "Error al comunicar con el servidor."}

# metodo de respuesta POST que recibe un json con un usuario y lo agrega a la api, retorna un json con un string de confirmacion
# params: usuario -> dict -> {_id, Nombre, Contraseña} -> "_id es el rut"
# return: dict -> {respuesta: "Usuario agregado" o "Usuario ya existe"}
def post_usuarios_event(CH_Gusuario: dict):
    try:
        CH_Gresponse = requests.post(f"{url}/usuarios/add", json=CH_Gusuario)
        return CH_Gresponse.json()
    except requests.exceptions.RequestException:
        return {"respuesta": "Error al comunicar con el servidor."}

