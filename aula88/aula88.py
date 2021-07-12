import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120) #nrows nn considera a linha de cabeçalho
dados.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos']

a = dados[["time","pontos"]].head()
print(a)

print("\n================\n")

b = dados.time.head()
print(b)

print("\n================\n")

dados_pos_tim_pts = dados[["posicao", "time", "pontos"]].head()
print(dados_pos_tim_pts)

print("\n================\n")

dados["aproveitamento"] = (dados["pontos"] * 100)/114

print(dados.head(20))