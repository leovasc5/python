import numpy as np
import pandas as pd

teste = pd.Series([1,2,3,4,5,6,7,8,9,10], name="Contagem")
print(type(teste))

print("\n")

#Converter Series para array
teste = teste.array
print(teste)

print("\n")

teste2 = pd.Series([10, -13, 6, 3, 87])
teste3 = pd.Series([1, -5, -4, 67, 4])

adicao = teste2 + 1
sub = teste2 - 2
mult = teste2 * 3
div = teste2 / 2
print(adicao)
print(sub)
print(mult)
print(div)

print("\n")

teste4 = teste2 + teste3
print(teste4)

print("\n")

print(np.average(teste3)) #Calcula a média pelo Numpy

print("\n")

print(teste2[teste2 > teste3])

print("\n")

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

print(type(dados["time"])) #retorna como Series -> Coluna
print(type(dados["time"])) #retorna como DataFrame -> Tabela
