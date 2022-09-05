import pandas as pd #Pandas
from sklearn import tree
import streamlit as st


st.title('Árvores de decisão')


dfTenis = pd.DataFrame({
'Tempo'       : ['Chuvoso', 'Ensolarado', 'Ensolarado', 'Nublado', 'Chuvoso',
                 'Chuvoso', 'Nublado', 'Nublado', 'Ensolarado', 'Chuvoso',
                 'Nublado', 'Ensolarado',
                 'Ensolarado', 'Chuvoso'],
'Temperatura' : [22, 21, 27, 28, 21, 
                 18, 18, 22, 24, 20, 
                 27, 29, 22, 24],
'Umidade'     : [91,72,90,86,96,
                 70,65,90,70,80,
                 75,85,95,80],
'Vento'       : ['Sim','Não','Sim','Não','Não',
                 'Sim','Sim','Sim','Sim','Não',
                 'Não','Não','Não','Não'],
'Jogo'        : ['Não','Sim','Não','Sim','Sim',
                 'Não','Sim','Sim','Sim','Sim',
                 'Sim','Não','Não','Sim']
})

quali = ['Tempo', 'Vento'] #Variáveis qualitativas
quant = ['Temperatura', 'Umidade'] #Variáveis quantitativas

dfQualiDummies = pd.get_dummies(dfTenis[quali]) #Dataframe com qualitativas dummy
dfQuant = dfTenis[quant] #Dataframe com quantitativas

dfWork = pd.concat([dfQualiDummies, dfQuant ], axis=1 ) #Dataframe com quali dummy e quant
target = dfTenis['Jogo']

arv = tree.DecisionTreeClassifier() #árvore de classificação
arv.fit(dfWork, target)

vento = st.radio('Tem vento?', ['Sim', 'Não'])
tempo = st.selectbox('Selecione o tempo', ['Chuvoso', 'Ensolarado', 'Nublado'])
temperatura = st.number_input('qual é a temperatura (°C)', value=0)
umidade = st.number_input('qual é umidade ', value=0)

# inicia com todos iguais a 0 para depois alterar
vals = [
    0,  #Tempo_Chuvoso
    0,  #Tempo_Ensolarado
    0,  #Tempo_Nublado
    0,  #Vento_Não
    0,  #Vento_Sim
    int(temperatura), #Temperatura
    int(umidade)  #Umidade
]

op_tempo = {
    'Chuvoso': vals[0],
    'Ensolarado': vals[1],
    'Nublado': vals[2]
}

op_vento = {
    'Não': vals[3],
    'Sim': vals[4]
}

op_tempo[tempo] = 1
op_vento[vento] = 1

res = arv.predict([vals])

if res[0] == 'Sim':
    st.write("Sim haverá jogo.")
else:
    st.write("Não haverá jogo.")