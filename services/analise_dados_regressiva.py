import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import db
import pandas as pd

from sklearn.linear_model import LinearRegression

import plotly.express as px

def analise_regressiva(id_plano):
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
            SELECT
                mes_referencia,
                preco_mensal,
                quantidade_assinantes
            FROM historico_planos
            WHERE id_plano = %s
            ORDER BY mes_referencia;
        """, (id_plano,))

    lista = cursor.fetchall()

    cursor.close()

    df = pd.DataFrame(lista)

    x = df[["preco_mensal"]]
    y = df["quantidade_assinantes"]


    modelo = LinearRegression()

    modelo.fit(x, y)


    df["previsao"] = modelo.predict(x)

    # Criar gráfico
    fig = px.scatter(
        df,
        x="preco_mensal",
        y="quantidade_assinantes",
        title="Relação entre preço e quantidade de assinantes",
        labels={
            "preco_mensal": "Preço mensal (R$)",
            "quantidade_assinantes": "Quantidade de assinantes"
        },
        hover_data=["mes_referencia"]
    )

    # Adicionar linha de regressão
    df_linha = df.sort_values("preco_mensal")

    fig.add_scatter(
        x=df_linha["preco_mensal"],
        y=df_linha["previsao"],
        mode="lines",
        name="Regressão linear"
    )

    return fig.to_json()