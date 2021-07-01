from numpy import nan
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd

alunos = {
    "Nome": ['Ricardo', 'Pedro', 'Roberto', 'Carlos', 'Amaral', 'Bernardo', 'Leandro'],
    "Nota": [4, 7, 9, 9.7, nan, 6.8, nan],
    "Aprovado":['Não', 'Sim', 'Sim', 'Sim', nan, 'Sim', nan]
}

df = pd.DataFrame(alunos)
df_faltantes = df.isnull()
print(df_faltantes.head(7))

faltantes = (df_faltantes.isnull().sum() / len(df_faltantes['Nome'])) #mostra a porcentagem de quantos dados faltam
#print(faltantes)

df = df.dropna() #-> Excluirá as linhas com dados faltantes
#print(df.head())
