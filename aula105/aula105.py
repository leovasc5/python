import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

def div(gols, partidas):
    return gols / partidas

media = dados.assign(media_gols = lambda x: div(dados["gols pro"], dados["partidas"]))
dados = media
print(dados)