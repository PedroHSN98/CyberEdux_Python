import streamlit as st  # Importa o módulo Streamlit para criar a interface web
import pandas as pd     # Importa a biblioteca pandas para manipulação de dados
import seaborn as sns   # Importa a biblioteca Seaborn para gráficos estatísticos
import matplotlib.pyplot as plt  # Importa o Matplotlib para criação de gráficos

# Configurações iniciais da interface
st.set_page_config(page_title="Análise de Consumo Elétrico", layout="wide")  # Define título da aba e layout da página
st.title("⚡ Análise de Consumo Elétrico no Brasil (2006–2020)")  # Exibe o título principal no topo da página

# Carrega o dataset CSV com os dados de consumo
df = pd.read_csv("consumo_eletrico_streamlit.csv")  # Lê o arquivo CSV com os dados e armazena em um DataFrame

# Conversão de colunas numéricas (anos, população e temperatura)
anos = [str(ano) for ano in range(2006, 2021)]  # Cria lista com os anos de 2006 a 2020 como strings
df[anos] = df[anos].apply(pd.to_numeric, errors="coerce")  # Converte os dados de consumo por ano para valores numéricos
df["populacao"] = pd.to_numeric(df["populacao"], errors="coerce")  # Converte a coluna população para número
df["temp_media"] = pd.to_numeric(df["temp_media"], errors="coerce")  # Converte a temperatura média para número

# Cálculos adicionais
df["total_consumo"] = df[anos].sum(axis=1)  # Soma o consumo de todos os anos para cada linha (localidade)
df["crescimento"] = df["2020"] - df["2006"]  # Calcula o crescimento do consumo entre 2006 e 2020

# Cria um menu lateral com as opções de gráfico
opcao = st.sidebar.selectbox(  # Cria um dropdown na barra lateral para escolher o gráfico
    "Selecione o gráfico que deseja visualizar:",
    [
        "📈 Consumo Médio ao Longo dos Anos",     # Opção 1
        "🌱 Consumo Total por Bioma",             # Opção 2
        "👥 População vs Consumo Total",          # Opção 3
        "🌡️ Temperatura Média vs Consumo Total", # Opção 4
        "🚀 Top 10 Crescimento de Consumo"        # Opção 5
    ]
)

# === GRÁFICO 1 ===
if opcao == "📈 Consumo Médio ao Longo dos Anos":
    st.subheader("📈 Consumo Elétrico Médio ao Longo dos Anos")  # Subtítulo da seção
    st.caption("📈 Gráfico 1 - Tipo: **Descritivo e Demonstrativo**. Mostra a média de consumo de energia elétrica anual no Brasil (2006–2020).")  # Descrição

    media_anual = df[anos].mean()  # Calcula a média do consumo em cada ano
    fig, ax = plt.subplots(figsize=(10, 4))  # Cria uma figura com tamanho específico
    sns.lineplot(x=media_anual.index.astype(str), y=media_anual.values, marker="o", ax=ax)  # Gera gráfico de linha

    for ano, valor in zip(media_anual.index.astype(str), media_anual.values):  # Adiciona valores sobre os pontos
        ax.text(ano, valor + (max(media_anual.values) * 0.01), f"{valor:.2f}", ha='center', va='bottom', fontsize=8, color='black')

    ax.set_xlabel("Ano")  # Rótulo do eixo X
    ax.set_ylabel("Consumo Médio")  # Rótulo do eixo Y
    ax.set_title("Consumo Elétrico Médio por Ano (Brasil)")  # Título do gráfico
    ax.grid(True)  # Ativa a grade de fundo
    st.pyplot(fig)  # Exibe o gráfico no Streamlit

# === GRÁFICO 2 ===
elif opcao == "🌱 Consumo Total por Bioma":
    st.subheader("🌱 Consumo Total por Bioma")  # Subtítulo da seção
    st.caption("🌱 Gráfico 2 - Tipo: **Descritivo e Demonstrativo**. Compara o total consumido por bioma de 2006 a 2020, com exibição detalhada por bioma.")  # Descrição

    bioma_consumo = df.groupby("bioma")["total_consumo"].sum().sort_values(ascending=False)  # Soma o total por bioma e ordena decrescente

    fig, ax = plt.subplots(figsize=(10, 4))  # Cria figura
    sns.barplot(x=bioma_consumo.index, y=bioma_consumo.values, ax=ax)  # Cria gráfico de barras
    ax.set_xlabel("Bioma")  # Eixo X
    ax.set_ylabel("Consumo Total (GWh)")  # Eixo Y
    ax.set_title("Consumo Total por Bioma (2006–2020)")  # Título
    ax.tick_params(axis='x', rotation=45)  # Rotaciona os nomes dos biomas
    st.pyplot(fig)  # Mostra o gráfico

    st.markdown("### 🔢 Consumo Total por Bioma (valores numéricos)")  # Título da tabela
    st.dataframe(bioma_consumo.reset_index().rename(columns={
        "bioma": "Bioma",
        "total_consumo": "Consumo Total (GWh)"
    }))  # Exibe os dados em formato de tabela interativa

# === GRÁFICO 3 ===
elif opcao == "👥 População vs Consumo Total":
    st.subheader("👥 População vs Consumo Total")  # Subtítulo
    st.caption("👥 Gráfico 3 - Tipo: **Demonstrativo**. Mostra a relação entre o tamanho da população e o total consumido.")  # Descrição

    fig, ax = plt.subplots(figsize=(8, 5))  # Figura
    sns.scatterplot(data=df, x="populacao", y="total_consumo", ax=ax)  # Gráfico de dispersão
    ax.set_title("População vs Consumo Total")  # Título
    ax.set_xlabel("População")  # Eixo X
    ax.set_ylabel("Consumo Total")  # Eixo Y
    ax.grid(True)  # Grade
    st.pyplot(fig)  # Exibe gráfico

# === GRÁFICO 4 ===
elif opcao == "🌡️ Temperatura Média vs Consumo Total":
    st.subheader("🌡️ Temperatura Média vs Consumo Total")  # Subtítulo
    st.caption("🌡️ Gráfico 4 - Tipo: **Demonstrativo**. Analisa se regiões mais quentes consomem mais energia.")  # Descrição

    fig, ax = plt.subplots(figsize=(8, 5))  # Figura
    sns.scatterplot(data=df, x="temp_media", y="total_consumo", ax=ax)  # Gráfico de dispersão
    ax.set_title("Temperatura Média vs Consumo Total")  # Título
    ax.set_xlabel("Temperatura Média (°C)")  # Eixo X
    ax.set_ylabel("Consumo Total")  # Eixo Y
    ax.grid(True)  # Grade
    st.pyplot(fig)  # Exibe gráfico

# === GRÁFICO 5 ===
elif opcao == "🚀 Top 10 Crescimento de Consumo":
    st.subheader("🚀 Top 10 Crescimento de Consumo")  # Subtítulo
    st.caption("🚀 Gráfico 5 - Tipo: **Descritivo e Demonstrativo**. Exibe as 10 localidades com maior aumento no consumo elétrico entre 2006 e 2020.")  # Descrição

    top_crescimento = df.sort_values(by="crescimento", ascending=False).head(10)  # Filtra top 10 com maior crescimento
    top_crescimento["localidade"] = top_crescimento.index.astype(str) + " - " + top_crescimento["bioma"]  # Cria nova coluna com nome + bioma
    top_crescimento = top_crescimento.reset_index(drop=True)  # Reseta o índice

    fig, ax = plt.subplots(figsize=(12, 5))  # Figura
    bars = sns.barplot(x=top_crescimento["localidade"], y=top_crescimento["crescimento"], ax=ax)  # Gráfico de barras

    ax.set_xlabel("Localidade (Estado - Bioma)")  # Eixo X
    ax.set_ylabel("Crescimento (GWh)")  # Eixo Y
    ax.set_title("Top 10 Localidades com Maior Crescimento de Consumo (2006–2020)")  # Título
    ax.tick_params(axis='x', rotation=45)  # Rotaciona os nomes

    import matplotlib.ticker as ticker  # Importa para formatação numérica
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', '.')))  # Formata os valores no eixo Y

    for container in bars.containers:  # Adiciona valores nas barras
        bars.bar_label(container,
                       labels=[f'{int(v):,}'.replace(',', '.') for v in container.datavalues],
                       padding=3,
                       fontsize=9,
                       color='black')

    st.pyplot(fig)  # Exibe gráfico
