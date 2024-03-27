

import requests

url = "http://50.16.153.222:8081/events" # Coloca la dirección URL de tu API Flask aquí

params = {
    "username": "jorge",
    "password": "ufro"
}

response = requests.post(url, json=params)

get = requests.get(url)

if response.ok:
    token = response.json()["token"]
    print("Token de autenticación recibido:", token)
else:
    print("Error al recibir la respuesta de la API")




#   def create_app():
#       app = Flask(__name__)
#       return app
#       app = create_app()

# metodo de respuesta GET para concoer el estado del servicio, devuelve un json
# para llamarlo poner SU_IP:8081/status

#   @app.route("/status")
#   def status():
#       return {
#           "estado": "1",
#           "texto": "OK" 
#   }

# API REST que recibe un JSON lo imprime por consola y responde un json 
    
#   @app.route("/events", methods=(['POST']))
#   def create_event():
#       event = request.json
#       print(event)
#       response = {'token': '123456789'}
#       return jsonify(response)
#   if __name__ == '__main__':
#       app.run(host="0.0.0.0", port=8081, debug=True) #levanta el servicio REST API en puerto 808

