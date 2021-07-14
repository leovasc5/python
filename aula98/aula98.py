import pandas as pd
import numpy as np

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

print(dados[["posicao", "time", "pontos"]][0:20]) 
print(dados["time"][0])
dados["teste"] = "Valor Teste"
print(dados.head())

dados["aprov."] = (dados["pontos"] * 100) /114
print(dados.head())

del dados["aprov."] #APAGA A COLUNA
print(dados.head())

dados["aprov."] = (dados["pontos"] * 100) /114
aprov = dados.pop("aprov.") #CORTA PARA UM NOVO LUGAR
print(dados.head())
print(aprov)