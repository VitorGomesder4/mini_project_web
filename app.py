from flask import Flask, render_template, request, jsonify, session, url_for
from models.user import User
from models.usuariosite import UserSite
from dotenv import load_dotenv
import os

load_dotenv()

from database import db
from routes.tabelas.usuarios import usuarios_bp
from routes.tabelas.assinaturas import assinaturas_bp
from routes.tabelas.planos import planos_bp
from routes.tabelas.historico_planos import historico_planos_bp

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

app.register_blueprint(usuarios_bp)
app.register_blueprint(assinaturas_bp)
app.register_blueprint(planos_bp)
app.register_blueprint(historico_planos_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home", methods=["GET"])
def home():
    return render_template("usuarioAutenticado.html")

@app.route("/registrar", methods=['GET'])
def r_registrar():
    return render_template("registro.html")

@app.route("/registrar", methods=['POST'])
def registrar():
    data = request.get_json()

    try:
        data["nome"], data["data_nascimento"], data["sexo"] = data["nome"].strip(), data["data_nascimento"].strip(), data["sexo"].strip()
    except AttributeError as erro:
        return jsonify({"message": str(erro)}), 400

    campos_must = {"nome", "data_nascimento", "sexo"}

    if not data or not campos_must.issubset(data.keys()):
        return jsonify({"message": "Campos de formulario faltando ou formulario inexistente"}), 400

    try:
        new_user = User(data["nome"], data["data_nascimento"], data["sexo"])
    except ValueError as erro:
        return jsonify({"message": str(erro)}), 400

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

@app.route("/cadastrar", methods=['GET'])
def get_cadastrar():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    data = request.get_json()

    try:
        data["username"], data["email"], data["password"] = data["username"].strip(), data["email"].strip(), data["password"].strip()
    except AttributeError:
        return jsonify({"message": str(AttributeError)}), 400

    campos_must = {"username", "email", "password"}

    if not data or not campos_must.issubset(data.keys()):
        return jsonify({"message": "Campos de formulario faltando ou formulario inexistente"}), 400

    try:
        if data["username"] != "" and data["password"] != "":
            new_user_s = UserSite(data["username"], data["email"], data["password"])
    except ValueError as erro:
        return jsonify({"message": str(erro)}), 400

    if new_user_s.email == "":
        email = None
    else:
        email = new_user_s.email

    cursor = db.cursor()

    cursor.execute(
        "SELECT id_user_site FROM USER_SITE WHERE username = %s",
        (new_user_s.username,)
    )

    search_query = cursor.fetchone()

    if search_query:
        return jsonify({"message": "Nome de usuario ja cadastrado"})

    cursor.execute(
        """
        INSERT INTO USER_SITE (username, email, password)
        VALUES (%s, %s, %s)
        """, 
        (new_user_s.username, email, new_user_s.password)
        )

    db.commit()
    cursor.close()

    return jsonify({"message": "Usuario do Site cadastrado com sucesso"}), 200


@app.route("/login", methods=["POST"])
def logar():
    data = request.get_json()

    campos_must = {"loginCredential", "passwordCredential"}

    if not data or not campos_must.issubset(data.keys()):
        return jsonify({"message": "Campos necessarios faltando no json"}), 400

    if data["loginCredential"] != "" and data["passwordCredential"] != "":
        cursor = db.cursor()

        cursor.execute(
                "SELECT id_user_site, password FROM USER_SITE WHERE username = %s or email = %s",
                (data["loginCredential"], data["loginCredential"])
            )

        search_query = cursor.fetchone()

        if not search_query:
                return jsonify({"message": "Login inexistente tente novamente"}), 400

        if data["passwordCredential"] != search_query[1]:
            return jsonify({"message": "Senha incorreta"}), 400


        session.clear()
        session["id_user_site"] = search_query[0]

        print(session)

        return jsonify({"message": "Login validado", "redirect": url_for("home")}), 200

    else:
        return jsonify({"message": "1 ou mais campos necessarios vazios"}), 400


if __name__ == "__main__":
    app.run(debug=True)