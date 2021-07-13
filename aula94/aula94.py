import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

print(dados.vitorias.min())
print(dados.vitorias.max())
print(dados[dados.posicao == 1].pontos.mean())
#print(dados[["vitorias", "pontos", "time"]].groupby(["time", "pontos"]).mean()) -> Em casos de dados com mais informações
print(dados[["vitorias", "pontos", "time"]].groupby(["time"]).mean())
colunas = ["vitorias", "pontos"]
print(dados[(dados.vitorias >= 23) & (dados.derrotas <= 8)].head(15))