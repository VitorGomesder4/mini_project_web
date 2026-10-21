from flask import Blueprint, request, jsonify
from database import db

planos_bp = Blueprint("planos", __name__)

@planos_bp.route("/planos", methods=["GET"])
def get_planos():

    inicio = request.args.get("inicio", default=0, type=int)
    fim = request.args.get("fim", default=20, type=int)

    limite = fim - inicio
    offset_ = inicio

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT id_plano, nome_plano, preco_mensal,
               qualidade_video, telas_simultaneas
        FROM planos
        ORDER BY id_plano
        LIMIT %s OFFSET %s
    """, (limite, offset_))

    lista_planos = cursor.fetchall()

    cursor.close()

    print(lista_planos)

    return jsonify(lista_planos), 200