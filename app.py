from flask import Flask, render_template, request, jsonify
from models.user import User
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

db = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_DATABASE)

print(db)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/registrar", methods=['GET'])
def r_registrar():
    return render_template("registro.html")

@app.route("/registrar", methods=['POST'])
def registrar():
    data = request.get_json()

    try:
        data["nome"], data["data_nascimento"], data["sexo"] = data["nome"].strip(), data["data_nascimento"].strip(), data["sexo"].strip()
    except AttributeError:
        return jsonify({"message": str(AttributeError)}), 400

    campos_must = {"nome", "data_nascimento", "sexo"}

    if not data or not campos_must.issubset(data.keys()):
        return jsonify({"message": "Campos de formulario faltando ou formulario inexistente"}), 400

    try:
        new_user = User(data["nome"], data["data_nascimento"], data["sexo"])
    except ValueError:
        return jsonify({"message": str(ValueError)}), 400

    if new_user.data_nascimento == "":
        data_nascimento = None
    else:
        data_nascimento = new_user.data_nascimento

    if new_user.sexo == "":
        sexo = None
    else:
        sexo = new_user.sexo

    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO USER (nome, data_nascimento, sexo)
        VALUES (%s, %s, %s)
        """, 
        (new_user.nome, data_nascimento, sexo)
        )

    db.commit()
    cursor.close()

    return jsonify({"message": "Usuario cadastrado com sucesso"}), 200

if __name__ == "__main__":
    app.run(debug=True)