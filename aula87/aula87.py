import pandas as pd

dados = pd.read_excel("C:/Users/l5/python/aula38/planilha1.xlsx", sheet_name="Planilha2") #sheet_name -> define a aba da planilha
                                                                  #sheet_name=0 | sheet_name=1
print(dados.head(6))

arquivo_excel = pd.ExcelFile("C:/Users/l5/python/aula38/planilha1.xlsx")

aba1 = arquivo_excel.parse("Planilha1")
print(aba1.head())

aba2 = arquivo_excel.parse("Planilha2")
print(aba2.head())

dados1 = pd.read_excel("C:/Users/l5/python/aula38/planilha1.xlsx", sheet_name="Planilha1")
print(dados1.head())

dados2 = pd.read_excel("C:/Users/l5/python/aula38/planilha1.xlsx", sheet_name="Planilha2")
print(dados2.head())