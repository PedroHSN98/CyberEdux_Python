import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Configurações iniciais
st.set_page_config(page_title="Análise de Consumo Elétrico", layout="wide")
st.title("⚡ Análise de Consumo Elétrico no Brasil (2006–2020)")

# Carregando o dataset
df = pd.read_csv("consumo_eletrico_streamlit.csv")

# Conversão de colunas numéricas
anos = [str(ano) for ano in range(2006, 2021)]
df[anos] = df[anos].apply(pd.to_numeric, errors="coerce")
df["populacao"] = pd.to_numeric(df["populacao"], errors="coerce")
df["temp_media"] = pd.to_numeric(df["temp_media"], errors="coerce")

# Total de consumo por linha
df["total_consumo"] = df[anos].sum(axis=1)
df["crescimento"] = df["2020"] - df["2006"]

# Barra lateral com seleção
opcao = st.sidebar.selectbox(
    "Selecione o gráfico que deseja visualizar:",
    [
        "📈 Consumo Médio ao Longo dos Anos",     # Descritivo + Demonstrativo
        "🌱 Consumo Total por Bioma",             # Descritivo + Demonstrativo
        "👥 População vs Consumo Total",          # Demonstrativo
        "🌡️ Temperatura Média vs Consumo Total", # Demonstrativo
        "🚀 Top 10 Crescimento de Consumo"        # Descritivo + Demonstrativo
    ]
)

# Gráfico 1 - Consumo Elétrico Médio ao Longo dos Anos
# ➤ Tipo: Descritivo + Demonstrativo
if opcao == "📈 Consumo Médio ao Longo dos Anos":
    st.subheader("📈 Consumo Elétrico Médio ao Longo dos Anos")
    st.caption("📈 Gráfico 1 - Tipo: **Descritivo e Demonstrativo**. Mostra a média de consumo de energia elétrica anual no Brasil (2006–2020).")

    media_anual = df[anos].mean()
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(x=media_anual.index.astype(str), y=media_anual.values, marker="o", ax=ax)


    for ano, valor in zip(media_anual.index.astype(str), media_anual.values):
        ax.text(ano, valor + (max(media_anual.values) * 0.01), f"{valor:.2f}", 
                ha='center', va='bottom', fontsize=8, color='black')

    ax.set_xlabel("Ano")
    ax.set_ylabel("Consumo Médio")
    ax.set_title("Consumo Elétrico Médio por Ano (Brasil)")
    ax.grid(True)
    st.pyplot(fig)



# Gráfico 2 - Consumo Total por Bioma
#O 1e8 que aparece no eixo Y do gráfico "Consumo Total por Bioma" significa notação científica e indica que os valores estão sendo exibidos em múltiplos de 100 milhões (ou seja, 1×108 = 100.000.000 1 × 108 = 100.000.000).
# ➤ Tipo: Descritivo + Demonstrativo
elif opcao == "🌱 Consumo Total por Bioma":
    st.subheader("🌱 Consumo Total por Bioma")
    st.caption("🌱 Gráfico 2 - Tipo: **Descritivo e Demonstrativo**. Compara o total consumido por bioma de 2006 a 2020, com exibição detalhada por bioma.")

    # Agrupamento por bioma
    bioma_consumo = df.groupby("bioma")["total_consumo"].sum().sort_values(ascending=False)

    # Gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(x=bioma_consumo.index, y=bioma_consumo.values, ax=ax)
    ax.set_xlabel("Bioma")
    ax.set_ylabel("Consumo Total (GWh)")
    ax.set_title("Consumo Total por Bioma (2006–2020)")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # Exibição dos valores em forma de tabela
    st.markdown("### 🔢 Consumo Total por Bioma (valores numéricos)")
    st.dataframe(bioma_consumo.reset_index().rename(columns={
        "bioma": "Bioma",
        "total_consumo": "Consumo Total (GWh)"
    }))



# Gráfico 3 - População vs Consumo Total
# ➤ Tipo: Demonstrativo
elif opcao == "👥 População vs Consumo Total":
    st.subheader("👥 População vs Consumo Total")
    st.caption("👥 Gráfico 3 - Tipo: **Demonstrativo**. Mostra a relação entre o tamanho da população e o total consumido.")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x="populacao", y="total_consumo", ax=ax)
    ax.set_title("População vs Consumo Total")
    ax.set_xlabel("População")
    ax.set_ylabel("Consumo Total")
    ax.grid(True)
    st.pyplot(fig)


# Gráfico 4 – Temperatura Média vs Consumo Total
# ➤ Tipo: Demonstrativo
elif opcao == "🌡️ Temperatura Média vs Consumo Total":
    st.subheader("🌡️ Temperatura Média vs Consumo Total")
    st.caption("🌡️ Gráfico 4 - Tipo: **Demonstrativo**. Analisa se regiões mais quentes consomem mais energia.")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x="temp_media", y="total_consumo", ax=ax)
    ax.set_title("Temperatura Média vs Consumo Total")
    ax.set_xlabel("Temperatura Média (°C)")
    ax.set_ylabel("Consumo Total")
    ax.grid(True)
    st.pyplot(fig)


# Gráfico 5 - Top 10 Crescimento de Consumo
# ➤ Tipo: Descritivo + Demonstrativo
elif opcao == "🚀 Top 10 Crescimento de Consumo":
    st.subheader("🚀 Top 10 Crescimento de Consumo")
    st.caption("🚀 Gráfico 5 - Tipo: **Descritivo e Demonstrativo**. Exibe as 10 localidades com maior aumento no consumo elétrico entre 2006 e 2020, com visualização detalhada.")

    top_crescimento = df.sort_values(by="crescimento", ascending=False).head(10)
    top_crescimento["localidade"] = top_crescimento.index.astype(str) + " - " + top_crescimento["bioma"]
    top_crescimento = top_crescimento.reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(12, 5))
    bars = sns.barplot(x=top_crescimento["localidade"], y=top_crescimento["crescimento"], ax=ax)

    ax.set_xlabel("Localidade (Estado - Bioma)")
    ax.set_ylabel("Crescimento (GWh)")
    ax.set_title("Top 10 Localidades com Maior Crescimento de Consumo (2006–2020)")
    ax.tick_params(axis='x', rotation=45)

    import matplotlib.ticker as ticker
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', '.')))

    # Adiciona os valores acima das barras
    for container in bars.containers:
        bars.bar_label(container,
                       labels=[f'{int(v):,}'.replace(',', '.') for v in container.datavalues],
                       padding=3,
                       fontsize=9,
                       color='black')

    st.pyplot(fig)


    import matplotlib.ticker as ticker
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', '.')))

    for container in bars.containers:
        ax.bar_label(container, labels=[f'{int(v):,}'.replace(',', '.') for v in container.datavalues], padding=3)

    st.pyplot(fig)




