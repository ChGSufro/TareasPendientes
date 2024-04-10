from flask import Flask, jsonify, request #importa la libreria Flask, jsonify y request
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["Gestor_De_Tareas"]

Ch_G_Tareas = db["Tareas"]
Ch_G_Usuarios = db["Usuarios"]

#metodo que devuelve el id de la ultima tarea + 1
#return: int
def generar_id():
    lista_tareas = list(Ch_G_Tareas.find())
    if len(lista_tareas) == 0:
        return  1
    return lista_tareas[-1]["_id"] + 1

#metodo que recibe una tarea en formato diccionario y la agrega a la base de datos con un nuevo id unico.
#param: tarea -> dict -> {Usuario, Nombre, Descripcion, Estado}
def agregar_tarea(tarea):
    tarea["_id"] = generar_id()
    Ch_G_Tareas.insert_one(tarea)

#metodo que recibe un propietario y devuelve una lista con las tareas asociadas a ese propietario.
#param: propietario -> str -> rut del propietario de las tareas
#return: list -> dict{_id, Usuario, Nombre, Descripcion, Estado}
def extraer_tareas(propietario):
    lista_tareas = list(Ch_G_Tareas.find({"Usuario": propietario}))
    return lista_tareas

#metodo que recibe una tarea en formato diccionario y la modifica en la base de datos.
#param: tarea -> dict -> {_id, Usuario, Nombre, Descripcion, Estado}
#return: str -> "Tarea modificada." o "Tarea no encontrada."
def modificar_tarea(tarea):
    tarea_id = tarea["_id"]
    tarea.pop("_id")
    Ch_G_Tareas.update_one({"_id": tarea_id}, {"$set": tarea})
    return "Tarea modificada."

#metodo que recibe un id y elimina la tarea asociada a ese id en la coleccón de tareas.
#param: id -> int -> id de la tarea a eliminar
#return: str -> "Tarea eliminada." o "Tarea no encontrada."
def eliminar_tarea(id):
    Ch_G_Tareas.delete_one({"_id": id})
    return "Tarea eliminada."

#metodo que recibe un id y verifica si existe en la colección devolviendo un booleano.
#param: id -> str -> rut del usuario
#return: bool
def usuario_existe(rut):
    if Ch_G_Usuarios.find_one({"_id": rut}) != None:
        return True
    return False

#metodo que recibe un rut y una contraseña y verifica si el usuario existe y la contraseña es correcta.
#param: rut -> str -> rut del usuario
#param: contraseña -> str -> contraseña del usuario
#return: dict -> {_id, Nombre} "_id = rutkey" o str -> "Usuario y/o contraseña incorrectos" 
def extraer_usuario(rut, contraseña):
    usuario = Ch_G_Usuarios.find_one({"_id": rut})
    if usuario["Contraseña"] == contraseña:
        return usuario
    return None

#metodo que recibe un usuario en formato diccionario y lo agrega a la lista de usuarios
#param: usuario -> dict -> {id_, Nombre, Contraseña}
def agregar_usuario(usuario):
    Ch_G_Usuarios.insert_one(usuario)

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

# metodo de respuesta GET para concoer el estado del servicio, devuelve un json
# para llamarlo poner SU_IP:8081/status
@app.route("/status")
def status():
    return {
        "estado": "1",
        "texto": "OK" 
}

# API REST que recibe un JSON lo imprime por consola y responde un json
@app.route("/events", methods=(['POST'])) 
def create_event():
    event = request.json
    print(event)
    response = {'token': '123456789'}
    return jsonify(response)


#metodo get encargado de devolver un json con la lista de tareas
#ruta para llamarlo: SU_IP:8081/tareas/get/<propietario> -> rut propietario de las tareas
#return: json -> {respuesta: {_id, Usuario, Nombre, Descripcion, Estado} }
@app.route("/tareas/get/<propietario>", methods=(['GET']))
def get_tareas(propietario):
        CH_tareas = extraer_tareas(propietario)
        return jsonify({"respuesta": CH_tareas})

#metodo post encargado de agregar una tarea nueva.
#ruta para llamarlo: SU_IP:8081/tareas/add
#request: tarea -> dict -> {Usuario, Nombre, Descripcion, Estado}
#return: json -> {respuesta: "Tarea agregada."}
@app.route("/tareas/add", methods=(['POST']))
def post_tareas():
    CH_tarea = request.json
    agregar_tarea(CH_tarea)
    return jsonify({"respuesta": "Tarea agregada."})

#metodo put encargado de modificar una tarea.
#ruta para llamarlo: SU_IP:8081/tareas/update
#request: tarea -> dict -> {_id, Usuario, Nombre, Descripcion, Estado}
#return: json -> {respuesta: "Tarea modificada." o "Tarea no encontrada."}
@app.route("/tareas/update", methods=(['PUT']))
def put_tareas():
    CH_tarea = request.json
    return jsonify({"respuesta": modificar_tarea(CH_tarea)})

#metodo delete encargado de eliminar una tarea.
#ruta para llamarlo: SU_IP:8081/tareas/delete/<id> -> id de la tarea a eliminar
#return: json -> {respuesta: "Tarea eliminada." o "Tarea no encontrada."}
@app.route("/tareas/delete/<id>", methods=(['DELETE']))
def delete_tareas(id):
    return jsonify({"respuesta": eliminar_tarea(int(id))})

#metodo post que recibe un id de usuario y una contraseña y devuelve un json con el usuario si existe.
#ruta para llamarlo: SU_IP:8081/usuarios/log
#request: usuario -> dict -> {Rut, Contraseña}
#return: json -> {respuesta: {Rut, Nombre} o "Usuario y/o contraseña incorrectos"}
@app.route("/usuarios/log/", methods=(['POST']))
def post_usuarios_log():
    CH_usuario = request.json
    if usuario_existe(CH_usuario["_id"]):
        return jsonify({"respuesta": extraer_usuario(CH_usuario["_id"], CH_usuario["Contraseña"])})
    return jsonify({"respuesta": "Usuario y/o contraseña incorrectos."})

#metodo post que recibe un json con un usuario y lo agrega a la lista de usuarios en caso de no existir
#ruta para llamarlo: SU_IP:8081/usuarios/add
#request: usuario -> dict -> {Rut, Nombre, Contraseña}
#return: json -> {respuesta: "Usuario agregado" o "Usuario ya existe"}
@app.route("/usuarios/add", methods=(['POST']))
def post_usuarios():
    CH_usuario = request.json
    if usuario_existe(CH_usuario["_id"]):
        return jsonify({"respuesta": "Usuario ya existe"})
    agregar_usuario(CH_usuario)
    return jsonify({"respuesta": "Usuario agregado"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True) #levanta el servicio REST API en puerto 8081