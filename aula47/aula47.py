import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/l5/python/aula38/planilha2.csv')

df.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos',
 'xG','xG_diff','npxG','xGA','xGA_diff','npxGA','npxGD','ppda_coef','oppda_coef','deep','deep_allowed','xpts','xpts_diff']

excluir_colunas = ['xG','xG_diff','npxG','xGA','xGA_diff','npxGA','npxGD','ppda_coef','oppda_coef','deep','deep_allowed','xpts','xpts_diff']

for i in excluir_colunas:
    df.drop(i, axis=1, inplace=True)

tabela_la_liga14 = df.loc[df['liga'] == "La_liga"]
tabela_la_liga14 = tabela_la_liga14.loc[tabela_la_liga14['temporada'] == 2014]

x = np.arange(0, 115, 3) #Configuração de LI e LS da La Liga
y = np.arange(0, 115, 3) #Configuração de LI e LS da La Liga

times = tabela_la_liga14["time"]
pontos = tabela_la_liga14["pontos"]

plt.scatter(x,y)
plt.plot(times, pontos)
plt.show()