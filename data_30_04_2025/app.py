import streamlit as st
import pandas as pd
from datetime import datetime


def obter_dados():
    #fUNÇÃO QUE RETORNA O DATASET
    if 'df' in st.session_state.keys():
        return st.session_state.df
    else:
        with st.spinner('Carregando...'):
            df = pd.read_csv('dataset/powerconsumption.csv')
        st.session_state.df = df
        return st.session_state.df
    

def somador():
        with st.container(border=True):
            st.subheader('Calculadora de Soma')
            col1, col2 = st.columns(2)
            with col1:
                numl = st.number_input('Número A:', -100.0, 100.0, 0.0, 0.1)
            with col2:
            #nome = st.text_input('Digite seu nome:')
            #st.write(f'Olá, {nome}!')
            
                num2 = st.number_input(
                                label='Número B:', 
                                min_value=-100.0, 
                                max_value=100.0, 
                                value=0.0, 
                                step=0.1
                                )
            st.write('O resultado A + B é:', numl + num2)



    
def mostrar_dataset():
    df = pd.read_csv('dataset/powerconsumption.csv')
    st.subheader('Dataset de Consumo de Energia')
    with st.spinner(5):
        st.write('Carregando...')
        df['Datetime'] = pd.to_datetime(df['Datetime'], format='%m/%d/%Y %H:%M')
        data_selecionada = st.date_input('Data de leitura', value=datetime(year=2017, month=6, day=15),
            min_value=datetime(year=2017, month=1, day=1),
            max_value=datetime(year=2017, month=12, day=31)
    )
    df_ = df[df['Datetime'].dt.date == data_selecionada]
    st.write(df_na_data)      
        st.write(df)


    st.write(df)


def main():
     pg = st.navigation([
          st.Page(somador, title='Calculadora de Soma'),
            st.Page(mostrar_dataset, title='Mostrar Dataset')
     ])
     pg.run()
main()