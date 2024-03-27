from flask import Flask, jsonify, request #importa la libreria Flask, jsonify y request

#{Rut: {Nombre, Contraseña}}
USUARIOS = {
    "21290107-5" : {
    "Nombre": "Christian", 
    "Contraseña": "12345"
    }
}

#[{Id, Usuario, Nombre, Descripcion, Estado}]
TAREAS = [
    {
    "Id": 1001,
    "Usuario": "21290107-5", 
    "Nombre": "Tarea 1", 
    "Descripcion": "Descripcion de la tarea 1", 
    "Estado": "Pendiente"
    }
]

#metodo que recorre la lista de tareas y devuelve el id de la ultima tarea + 1
#return: int
def generar_id():
    if len(TAREAS) == 0:
        return 1
    return TAREAS[-1]["Id"] + 1

#metodo que recibe un propietario y devuelve una lista con las tareas asociadas a ese propietario.
#param: propietario -> str -> rut del propietario de las tareas
#return: list -> dict {Id, Usuario, Nombre, Descripcion, Estado}
def extraer_tareas(propietario):
    tareas = []
    for tarea in TAREAS:
        if tarea["Usuario"] == propietario:
            tareas.append(tarea)
    return tareas

#metodo que recibe una tarea en formato diccionario y la agrega a la lista de tareas con un nuevo id unico.
#param: tarea -> dict -> {Usuario, Nombre, Descripcion, Estado}
def agregar_tarea(tarea : dict):
    tarea["Id"] = generar_id()
    TAREAS.append(tarea)

#metodo que recibe una tarea en formato diccionario y la modifica en la lista de tareas
#param: new_tarea -> dict -> {Id, Usuario, Nombre, Descripcion, Estado}
#return: str -> "Tarea modificada." o "Tarea no encontrada."
def modificar_tarea(new_tarea : dict):
    for tarea in TAREAS:
        if tarea["Id"] == new_tarea["Id"]:
            tarea = new_tarea
            return "Tarea modificada."
    return "Tarea no encontrada."
    
#metodo que recibe un id y elimina la tarea asociada a ese id.
#param: id -> int -> id de la tarea a eliminar
#return: str -> "Tarea eliminada." o "Tarea no encontrada."
def eliminar_tarea(id):
    for tarea in TAREAS:
        if tarea["Id"] == id:
            TAREAS.remove(tarea)
            return "Tarea eliminada."
    return "Tarea no encontrada."

#metodo que recibe un id y verifica si existe en la lista de usuarios devolviendo un booleano.
#param: id -> str -> rut del usuario
#return: bool
def usuario_existe(id):
    if id in USUARIOS:
        return True
    return False

#metodo que recibe un id y una contraseña y verifica si el usuario existe y la contraseña es correcta.
#param: rut -> str -> rut del usuario
#param: contraseña -> str -> contraseña del usuario
#return: dict -> {Rut, Nombre} o str -> "Usuario y/o contraseña incorrectos"
def extraer_usuario(rut, contraseña):
    if USUARIOS[rut]["Contraseña"] != contraseña:
        return "Usuario y/o contraseña incorrectos"
    return {"Rut": rut, "Nombre": USUARIOS[rut]["Nombre"]}

#metodo que recibe un usuario en formato diccionario y lo agrega a la lista de usuarios
#param: usuario -> dict -> {Rut, Nombre, Contraseña}
def agregar_usuario(usuario : dict):
    usr = usuario
    rut = usuario["Rut"]
    del usuario["Rut"]
    USUARIOS[rut] = usr


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
#param: id -> str -> rut del propietario de las tareas
#return: json -> {respuesta: {Id, Usuario, Nombre, Descripcion, Estado} }
@app.route("/tareas/<id>", methods=(['GET']))
def get_tareas(id):
        tareas = extraer_tareas(id)
        return jsonify({"respuesta": tareas})

#metodo post encargado de agregar una tarea nueva
#param: tarea -> dict -> {Usuario, Nombre, Descripcion, Estado}
#return: json -> {respuesta: "Tarea agregada."}
@app.route("/tareas", methods=(['POST']))
def post_tareas():
    tarea = request.json
    agregar_tarea(tarea)
    return jsonify({"respuesta": "Tarea agregada."})

#metodo put encargado de modificar una tarea
#param: tarea -> dict -> {Id, Usuario, Nombre, Descripcion, Estado}
#return: json -> {respuesta: "Tarea modificada." o "Tarea no encontrada."}
@app.route("/tareas", methods=(['PUT']))
def put_tareas():
    tarea = request.json
    return jsonify({"respuesta": modificar_tarea(tarea)})

#metodo delete encargado de eliminar una tarea
#param: id -> int -> id de la tarea a eliminar
#return: json -> {respuesta: "Tarea eliminada." o "Tarea no encontrada."}
@app.route("/tareas/<id>", methods=(['DELETE']))
def delete_tareas(id):
    return jsonify({"respuesta": eliminar_tarea(int(id))})

# metodo post que recibe un id de usuario y una contraseña y devuelve un json con el usuario si existe
#param: usuario -> dict -> {Rut, Contraseña}
#return: json -> {respuesta: {Rut, Nombre} o "Usuario y/o contraseña incorrectos"}
@app.route("/usuarios/log/", methods=(['POST']))
def post_usuarios_log():
    usuario = request.json
    if usuario_existe(usuario["Rut"]):
        return jsonify({"respuesta": extraer_usuario(usuario["Rut"], usuario["Contraseña"])})
    return jsonify({"respuesta": "Usuario y/o contraseña incorrectos."})

#metodo post que recibe un json con un usuario y lo agrega a la lista de usuarios en caso de no existir
#param: usuario -> dict -> {Rut, Nombre, Contraseña}
#return: json -> {respuesta: "Usuario agregado" o "Usuario ya existe"}
@app.route("/usuarios/", methods=(['POST']))
def post_usuarios():
    usuario = request.json
    if usuario_existe(usuario["Rut"]):
        return jsonify({"respuesta": "Usuario ya existe"})
    agregar_usuario(usuario)
    return jsonify({"respuesta": "Usuario agregado"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True) #levanta el servicio REST API en puerto 8081