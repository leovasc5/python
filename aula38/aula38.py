import pandas as pd

dados = pd.read_excel('C:/Users/l5/python/aula38/planilha1.xlsx', engine="openpyxl")
print(dados.head(6))

dados2 = pd.read_csv('C:/Users/l5/python/aula38/planilha2.csv')
print(dados2.head(10))