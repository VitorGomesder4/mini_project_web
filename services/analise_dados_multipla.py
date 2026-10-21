
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from database import db


def analise_multipla(id_plano):
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                mes_referencia,
                preco_mensal,
                quantidade_assinantes
            FROM historico_planos
            WHERE id_plano = %s
            ORDER BY mes_referencia
        """, (id_plano,))

        dados = cursor.fetchall()

    finally:
        cursor.close()

    df = pd.DataFrame(dados)

    if df.empty:
        raise ValueError("Não existem dados para realizar a regressão múltipla.")

    # Garantir que as colunas tenham os tipos corretos
    df["mes_referencia"] = pd.to_datetime(df["mes_referencia"])
    df["preco_mensal"] = pd.to_numeric(df["preco_mensal"])
    df["quantidade_assinantes"] = pd.to_numeric(
        df["quantidade_assinantes"]
    )

    df = df.dropna().sort_values("mes_referencia").reset_index(drop=True)

    if len(df) < 5:
        raise ValueError("Existem poucos registros para realizar a análise.")

    # Variável que representa a passagem do tempo em dias
    df["tempo"] = (
        df["mes_referencia"] - df["mes_referencia"].min()
    ).dt.days

    # Extrair o mês para representar a sazonalidade
    df["mes_numero"] = df["mes_referencia"].dt.month

    # Criar variáveis numéricas para cada mês do ano
    meses = pd.get_dummies(
        df["mes_numero"],
        prefix="mes",
        drop_first=True,
        dtype=int
    )

    # Variáveis utilizadas para realizar a previsão
    X = pd.concat(
        [
            df[["preco_mensal", "tempo"]],
            meses
        ],
        axis=1
    )

    # Valor que o modelo tentará prever
    y = df["quantidade_assinantes"]

    # Treinar o modelo
    modelo = LinearRegression()
    modelo.fit(X, y)

    # Calcular a quantidade estimada de assinantes
    df["previsao"] = modelo.predict(X)

    # Avaliar o ajuste do modelo aos dados utilizados
    r2 = r2_score(y, df["previsao"])

    print("Regressão linear múltipla")
    print(f"Coeficiente do preço: {modelo.coef_[0]:.4f}")
    print(f"Coeficiente do tempo: {modelo.coef_[1]:.4f}")
    print(f"Intercepto: {modelo.intercept_:.4f}")
    print(f"R²: {r2:.4f}")

    # Criar o gráfico
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["mes_referencia"],
            y=df["quantidade_assinantes"],
            mode="lines+markers",
            name="Assinantes reais"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["mes_referencia"],
            y=df["previsao"],
            mode="lines",
            name="Regressão múltipla"
        )
    )

    fig.update_layout(
        title="Regressão Linear Múltipla - Plano 1",
        xaxis_title="Mês de referência",
        yaxis_title="Quantidade de assinantes",
        legend_title="Dados",
        template="plotly_white"
    )

    # Retornar o gráfico em formato JSON para o Flask
    return fig.to_json()
