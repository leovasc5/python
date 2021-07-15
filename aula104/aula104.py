import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

dados["Teste"] = "Teste"
dados = dados.assign(novaColuna = 1)

colunas = ["vitorias", "pontos"]
dados["teste"] = dados.vitorias + dados.pontos
print(dados.head())