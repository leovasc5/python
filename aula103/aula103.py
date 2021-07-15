import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

dados["aproveitamento"] = (dados["pontos"] * 100) / 114
dados["aproveitamento"] = dados["aproveitamento"].astype(str)
dados["aproveitamento"] = dados["aproveitamento"].to_list()
lista = []

for i in dados["aproveitamento"]:
    x = slice(4)
    i = i[x] + "%"
    lista.append(i)

dados["aproveitamento"] = lista

print(dados.head())