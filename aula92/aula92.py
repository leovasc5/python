import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

print(dados.posicao == 1)

print("\n================\n")

print(dados[dados.posicao == 1].head(6))

print("\n================\n")

print(dados[(dados.pontos >= 88) & (dados.posicao != 1)][["posicao", "time", "pontos"]].head())

print("\n================\n")

print(dados[(dados.vitorias >= 25) & ((dados.pontos >= 80) | (dados.derrotas <= 5))].head())