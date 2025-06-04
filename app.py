from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde cualquier origen (importante para Flutter)

@app.route('/identify_nose', methods=['POST'])
def identify_nose():
    image = request.files.get('nose_image')
    if image:
        # Aquí colocarás tu modelo de reconocimiento y lógica
        # Por ahora ejemplo dummy:
        result = {
            "name": "Firulais",
            "breed": "Labrador",
            "message": "Perro identificado correctamente"
        }
        return jsonify(result)
    return jsonify({"message": "No se recibió imagen"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
