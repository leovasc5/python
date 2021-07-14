import pandas as pd
import numpy as np

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

teste = pd.Series([1,4, 8, 12, 16, 20.5], name="teste")
print(teste.head())

print("\n")

teste = pd.Series(["A","B", "8", "12", "16", "20.5"], name="teste")
print(teste.head())

print("\n")

teste = pd.Series(np.random.randn(4), index=["w", "x", "y", "z"])
print(teste.head())

print("\n")

teste = pd.Series({"nome":"Fernando", "idade":18, "pais":"Brasil"})
print(teste.head())
print(teste[2])

print("\n")

teste = teste[0:3]
print(teste.head())

print("\n")

teste = pd.Series({"nome":"Fernando", "idade":18, "pais":"Brasil"})
teste = teste[["nome", "pais"]]
print(teste.head())

print("\n")

teste = pd.Series([1,2,3,4,5,6,7,8,9,10], name="Contagem")
print(teste.head())