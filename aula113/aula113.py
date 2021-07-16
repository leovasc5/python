import pandas as pd

df = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
df.columns = ["liga","temporada","posicao","time","partidas","vitorias","empates","derrotas","gols pro","gols contra","pontos"]

a = {
    "liga":["Cameponato disputado"],
    "temporada":["Ano(s) em que os jogos foram disputados"],
    "posicao":["Posição na qual o time terminou o campeonato"],
    "time":["Nome da equipe"]
}

df2 = pd.DataFrame(a)
print(df2)

b = {
    "colunas":["liga", "temporada", "posicao", "time"],
    "descricao":["Cameponato disputado", "Ano(s) em que os jogos foram disputados", "Posição na qual o time terminou o campeonato", "Nome da equipe"],
    "tipo":["string", "int", "int", "string"]
}

df3 = pd.DataFrame(b)
print(df3)