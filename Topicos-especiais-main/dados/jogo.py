
#importanto as bibliotecas que serão ultilizadas
from this import d
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np

#introduzindo a imagem e o titulo
st.title('UEFA CHAMPIONS LEAGUE SEASON 2021-22')
st.subheader('A UEFA Champions League é uma competição anual de clubes de futebol organizada pela União das Associações Europeias de Futebol e disputada por clubes europeus de primeira divisão, decidindo os vencedores da competição através de uma fase de grupos de ida e volta para se qualificarem para um formato eliminatório a duas mãos e um único final da perna.')
st.image('https://wallpapers.com/images/hd/star-stadium-uefa-champions-league-v4x1jw6xp7oqahdh.jpg')

st.title('FASE DE GRUPOS DA TEMPORADA')
st.image('https://s2.glbimg.com/owZn1gI-5zE9jukFWKQhIXPNIeY=/0x0:900x900/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2022/j/P/Tk4ASpRGiOzpVE5Nhzdw/champions.jpeg')

#acessando a base de dados onde se encontrar os dados gols por jogadores


database_path = "dados/gols.csv"
df = pd.read_csv(database_path, sep=',')


database_path2 = "dados/estatisticas.csv"
df2 = pd.read_csv(database_path2, sep=',')


database_path3 = "dados/attacking.csv"

df3 = pd.read_csv(database_path3, sep=',')


database_path4 = "dados/goleiros.csv"
df4 = pd.read_csv(database_path4, sep=',')


#Mostrando os 10 Melhores Da Temporada em cada Categoria
st.write('10 artilheiros da Temporada', df.head(10))


st.write('10 Jogadores que mais jogaram na Temporada', df2.head(10))


st.write('10 Atacantes da Temporada', df3.head(10))


st.write('10 Goleiros da temporada', df4.head(10))
