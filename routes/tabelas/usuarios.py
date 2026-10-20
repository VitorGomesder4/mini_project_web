from flask import Blueprint, request, jsonify
from app import db

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["GET"])
def get_usuarios():

    inicio = request.args.get("inicio", default=0, type=int)
    fim = request.args.get("fim", default=20, type=int)

    limite = fim-inicio
    offset_ = inicio

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT id_user_site, username, email
        FROM USER_SITE
        ORDER BY id_user_site
        LIMIT %s OFFSET %s
    """, (limite, offset_))


    lista_usuarios = cursor.fetchall()

    cursor.close()

    print(lista_usuarios)

    return jsonify(lista_usuarios), 200