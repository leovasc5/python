import pandas as pd

dados = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)

dados.columns = [x.capitalize() for x in dados.columns.to_list()]
print(dados.head())