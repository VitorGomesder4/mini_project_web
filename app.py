from flask import Flask, render_template, request, jsonify
from models.user import User

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("registro.html")

@app.route("/registrar", methods=['POST'])
def registrar():
    data = request.get_json()

    campos_must = {"nome", "data_nascimento", "sexo"}

    if not data or not campos_must.issubset(data.keys()):
        return jsonify({"message": "Campos de formulario faltando ou formulario inexistente"}), 400

    try:
        new_user = User(data["nome"], data["data_nascimento"], data["sexo"])
    except ValueError:
        return jsonify({"message": str(ValueError)}), 400

    return jsonify({"message": "Usuario cadastrado com sucesso"}), 200

if __name__ == "__main__":
    app.run(debug=True)