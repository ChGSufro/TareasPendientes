from flask import Flask, jsonify, request

USUARIOS = {
    "21290107-5" : {
    "Nombre": "Christian", 
    "Contraseña": "12345"
    }
}

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
def generar_id():
    if len(TAREAS) == 0:
        return 1
    return TAREAS[-1]["Id"] + 1

#metodo que recibe un propietario y devuelve una lista con las tareas asociadas a ese propietario.
def extraer_tareas(propietario):
    tareas = []
    for tarea in TAREAS:
        if tarea["Usuario"] == propietario:
            tareas.append(tarea)
    return tareas

#metodo que recibe una tarea en formato diccionario y la agrega a la lista de tareas con un nuevo id unico.
def agregar_tarea(tarea : dict):
    tarea["Id"] = generar_id()
    TAREAS.append(tarea)

#metodo que recibe una tarea en formato diccionario y la modifica en la lista de tareas
def modificar_tarea(new_tarea : dict):
    for tarea in TAREAS:
        if tarea["Id"] == new_tarea["Id"]:
            tarea = new_tarea
            return "Tarea modificada."
    return "Tarea no encontrada."
    
#metodo que recibe un id y elimina la tarea asociada a ese id.
def eliminar_tarea(id):
    for tarea in TAREAS:
        if tarea["Id"] == id:
            TAREAS.remove(tarea)
            return "Tarea eliminada."
    return "Tarea no encontrada."

#metodo que recibe un id y verifica si existe en la lista de usuarios devolviendo un booleano.
def usuario_existe(id):
    if id in USUARIOS:
        return True
    return False

#metodo que recibe un id y una contraseña y verifica si el usuario existe y la contraseña es correcta.
def extraer_usuario(rut, contraseña):
    if USUARIOS[rut]["Contraseña"] != contraseña:
        return "Usuario y/o contraseña incorrectos"
    return {"Rut": rut, "Nombre": USUARIOS[rut]["Nombre"]}

#metodo que recibe un usuario en formato diccionario y lo agrega a la lista de usuarios
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


# metodo get encargado de devolver un json con la lista de tareas
@app.route("/tareas/<id>", methods=(['GET']))
def get_tareas(id):
        tareas = extraer_tareas(id)
        return jsonify({"respuesta": tareas})

# metodo post encargado de agregar una tarea nueva
@app.route("/tareas", methods=(['POST']))
def post_tareas():
    tarea = request.json
    agregar_tarea(tarea)
    return jsonify({"respuesta": "Tarea agregada."})

# metodo put encargado de modificar una tarea
@app.route("/tareas", methods=(['PUT']))
def put_tareas():
    tarea = request.json
    return jsonify({"respuesta": modificar_tarea(tarea)})

# metodo delete encargado de eliminar una tarea
@app.route("/tareas/<id>", methods=(['DELETE']))
def delete_tareas(id):
    return jsonify({"respuesta": eliminar_tarea(id)})

#  metodo post que recibe un id de usuario y una contraseña y devuelve un json con el usuario si existe
@app.route("/usuarios/log/", methods=(['POST']))
def post_usuarios_log():
    usuario = request.json
    if usuario_existe(usuario["Rut"]):
        return jsonify({"respuesta": extraer_usuario(usuario["Rut"], usuario["Contraseña"])})
    return jsonify({"respuesta": "Usuario y/o contraseña incorrectos."})

# metodo post que recibe un json con un usuario y lo agrega a la lista de usuarios en caso de no existir
@app.route("/usuarios/", methods=(['POST']))
def post_usuarios():
    usuario = request.json
    if usuario_existe(usuario["Rut"]):
        return jsonify({"respuesta": "Usuario ya existe"})
    agregar_usuario(usuario)
    return jsonify({"respuesta": "Usuario agregado"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True) #levanta el servicio REST API en puerto 8081