from flask import Blueprint, Response, jsonify, request

from services.analise_dados_regressiva import analise_regressiva
from services.analise_dados_multipla import analise_multipla

analise_regressiva_bp = Blueprint("analise_regressiva", __name__)
analise_multipla_bp = Blueprint("analise_multipla", __name__)


def _ler_id_plano():
    id_plano = request.args.get("id_plano", type=int)
    if id_plano is None:
        raise ValueError("Selecione um plano.")
    return id_plano

@analise_regressiva_bp.route("/analise_regressiva", methods=["GET"])
def get_analise_regressiva():
    try:
        grafico_json = analise_regressiva(_ler_id_plano())
    except ValueError as erro:
        return jsonify({"message": str(erro)}), 400

    return Response(grafico_json, mimetype="application/json")

@analise_multipla_bp.route("/analise_multipla", methods=["GET"])
def get_analise_multipla():
    try:
        grafico_json = analise_multipla(_ler_id_plano())
    except ValueError as erro:
        return jsonify({"message": str(erro)}), 400

    return Response(grafico_json, mimetype="application/json")