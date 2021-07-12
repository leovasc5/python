import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

maiores = dados.sort_values("pontos", ascending=False)
print(maiores.filter(items = ["time", "pontos"]).head(10))

print("\n================\n")

print(maiores.filter(like="tim").head(10))

print("\n================\n")

print(maiores.loc[maiores["pontos"] >= 90].head(15))