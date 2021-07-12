import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

print(dados.loc[0].head(11))

print("\n================\n")

print(dados.loc[0:20].head(20))

print("\n================\n")

print(dados.iloc[0:10, [2,3,10]].head(10))