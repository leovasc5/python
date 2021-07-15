import pandas as pd
import numpy as np

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
novos_nomes = ["liga","temporada","posicao","time","partidas","vitorias","empates","derrotas","gols pro","gols contra","pontos"]
colunas = dict((chave, valor) for chave, valor in zip(dados.columns.to_list(), novos_nomes))

dados = dados.rename(columns=colunas)

#["liga","temporada","posicao","time","partidas","vitorias","empates","derrotas","gols pro","gols contra","pontos"]

print(dados.head())