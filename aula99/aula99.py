import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

dados["liga"] = dados["liga"].apply(lambda x: x.replace("La_liga", "La Liga"))
print(dados.head())

dados["posicao"] = dados["posicao"].apply(str) #Converteu para string
dados["posicao"] = dados["posicao"] + "º"

novaTemp = []
for i in dados["temporada"]:
    if i == 2014:
        i = "14/15"
        novaTemp.append(i)
    elif i == 2015:
        i = "15/16"
        novaTemp.append(i)
    elif i == 2016:
        i = "16/17"
        novaTemp.append(i)
    elif i == 2017:
        i = "17/18"
        novaTemp.append(i)
    elif i == 2018:
        i = "18/19"
        novaTemp.append(i)
    elif i == 2019:
        i = "19/20"
        novaTemp.append(i)

dados["temporada"] = novaTemp
print(dados.head(120))