import requests

url = "http://50.16.153.222:8081"

# la llave para acceder al return de la api es: "respuesta"

# metodo de respuesta GET que recibe un rut y devuelve un json con las tareas asociadas a ese id
def get_tareas_event(rut):
    try:
        response = requests.get(f"{url}/tareas/{rut}")
        return response.json()
    except requests.exceptions.RequestException:
        return {"respuesta": "Error al comunicar con el servidor."}

# metodo de respuesta POST que recibe un json con una tarea y lo envia para agregalo a la api, 
def post_tareas_event(tarea):
    try:
        response = requests.post(f"{url}/tareas", json=tarea)
        return response.json()
    except requests.exceptions.RequestException:
        return {"respuesta": "Error al comnicar con el servidor."}

# metodo de respuesta PUT que recibe un json con una tarea y lo actualiza en la api, retorna un json con un string de confirmacion
def put_tareas_event(tarea):
    try:
        response = requests.put(f"{url}/tareas", json=tarea)
        return response.json()
    except requests.exceptions.RequestException:
        return {"respuesta": "Error al comunicar con el servidor."}

# metodo de respuesta DELETE que recibe un id y elimina la tarea asociada a ese id, retorna un json con un string de confirmacion
def delete_tareas_event(id):
    try:
        response = requests.delete(f"{url}/tareas/{id}")
        return response.json()
    except requests.exceptions.RequestException: 
        return {"respuesta": "Error al comunicar con el servidor."}

# metodo de respuesta POST que recibe un json con un usuario y lo envia a la api, retorna un json con el usuario logeado "formato json" si existe o un string si no existe
def log_usuario_event(usuario: dict):
    try:
        response = requests.post(f"{url}/usuarios/log", json=usuario)
        return response.json()
    except requests.exceptions.RequestException:
        return {"respuesta": "Error al comunicar con el servidor."}

# metodo de respuesta POST que recibe un json con un usuario y lo agrega a la api, retorna un json con un string de confirmacion
def post_usuarios_event(usuario: dict):
    try:
        response = requests.post(f"{url}/usuarios", json=usuario)
        return response.json()
    except requests.exceptions.RequestException:
        return {"respuesta": "Error al comunicar con el servidor."}

