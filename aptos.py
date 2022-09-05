# TOPICOS-DARLON
import pandas as pd
import numpy as np #Numpy
import pandas as pd #Pandas
import matplotlib.pyplot as plt #Matplotlib
from sklearn.linear_model import LinearRegression #Regressão linear
from sklearn import metrics #Cálculo do erro
import streamlit as st

rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')

st.title('Predição de preços de apartamentos')
bairro = st.selectbox('Escolha o bairro', rioAptos['bairro'].unique())
df = rioAptos[rioAptos['bairro'] == bairro]

df_quartos = df['quartos']
minimo = int(df_quartos.min())
maximo = int(df_quartos.max())
quartos = st.slider("Escolha a quantidade de quartos", minimo, maximo, value=minimo)

df_area = df['area']
minimo = int(df_area.min())
maximo = int(df_area.max())
area = st.slider("Escolha a área", minimo, maximo, value=minimo)

# predição
indep = df[['quartos', 'area']].values.reshape(-1, 2) # variável independente
dep = df['preco'].values.flatten() # variavel dependente

rl = LinearRegression()
rl.fit(indep, dep)

x = [[quartos], [area]] # valor para a variável independente
x_arr = np.array(x).reshape(-1, 2)
y_pred = rl.predict(x_arr)

st.write(f"Valor estimado: R$ {int(y_pred.flatten()):,.2f}")
