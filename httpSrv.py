from flask import Flask, request
import json

# Crea el servidor Flask
app = Flask(__name__)

# Define la ruta para la solicitud POST
@app.route('/post', methods=['POST'])
def post():
    # Obtiene los datos de la solicitud
    data = request.get_json()

    # Imprime los datos recibidos
    print(data)

    # Responde con un código de éxito
    return 'Recibido: {}'.format(data)

@app.route('/midi', methods=['POST'])
def midi():
    data = request.get_json()
    
    if data is None:
        data = json.loads(request.data)
        
    print(data)

    return "OK"

# Inicia el servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
