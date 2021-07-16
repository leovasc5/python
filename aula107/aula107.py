import pandas as pd
import numpy as np

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']
indices = pd.Series(np.arange(1, 121, 1))
dados = dados.set_index(indices)

print(dados.loc[1:20])
print(dados.iloc[0:len(dados.index), [2,3,10]])