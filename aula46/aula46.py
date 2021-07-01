import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/l5/python/aula38/planilha2.csv')

df.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos',
 'xG','xG_diff','npxG','xGA','xGA_diff','npxGA','npxGD','ppda_coef','oppda_coef','deep','deep_allowed','xpts','xpts_diff']

excluir_colunas = ['xG','xG_diff','npxG','xGA','xGA_diff','npxGA','npxGD','ppda_coef','oppda_coef','deep','deep_allowed','xpts','xpts_diff']

for i in excluir_colunas:
    df.drop(i, axis=1, inplace=True)

tabela_la_liga14 = df.loc[df['liga'] == "La_liga"]
tabela_la_liga14 = tabela_la_liga14.loc[tabela_la_liga14['temporada'] == 2014]

tabela_la_liga14.boxplot(column=["gols pro", "gols contra", "posicao", "pontos"])
print(tabela_la_liga14.head(20))
plt.show()