from flask import Blueprint, request, jsonify
from database import db

assinaturas_bp = Blueprint("usuarios", __name__)

@assinaturas_bp.route("/assinaturas", methods=["GET"])
def get_assinaturas():

    inicio = request.args.get("inicio", default=0, type=int)
    fim = request.args.get("fim", default=20, type=int)

    limite = fim - inicio
    offset_ = inicio

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT id_assinatura, id_user_site, id_plano,
               data_inicio, data_fim, status
        FROM assinaturas
        ORDER BY id_assinatura
        LIMIT %s OFFSET %s
    """, (limite, offset_))

    lista_assinaturas = cursor.fetchall()

    cursor.close()

    print(lista_assinaturas)

    return jsonify(lista_assinaturas), 200