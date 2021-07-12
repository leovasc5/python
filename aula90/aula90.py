import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

print(dados.sort_values("pontos", ascending=False).head(10)) #Peguei as maiores pontuações

maiores = dados.sort_values("pontos", ascending=False)
maiores = maiores.loc[maiores["time"] != "Barcelona"] 
maiores = maiores.loc[maiores["time"] != "Real Madrid"] 
maiores = maiores.loc[maiores["time"] != "Atletico Madrid"] 

print(maiores.head(10)) #Maiores pontuações sem os 3 grandes