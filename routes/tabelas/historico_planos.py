from flask import Blueprint, request, jsonify
from database import db

historico_planos_bp = Blueprint("historico_planos", __name__)


@historico_planos_bp.route("/historico_planos", methods=["GET"])
def get_historico_planos():

    inicio = request.args.get("inicio", default=0, type=int)
    fim = request.args.get("fim", default=20, type=int)

    limite = fim - inicio
    offset_ = inicio

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT id_historico, id_plano, mes_referencia,
               preco_mensal, quantidade_assinantes
        FROM historico_planos
        ORDER BY id_historico
        LIMIT %s OFFSET %s
    """, (limite, offset_))

    lista_historico = cursor.fetchall()

    cursor.close()

    print(lista_historico)

    return jsonify(lista_historico), 200