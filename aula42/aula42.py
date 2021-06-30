import pandas as pd

df = pd.read_csv('C:/Users/l5/python/aula38/planilha2.csv')

df.columns = ['Liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos',
 'xG','xG_diff','npxG','xGA','xGA_diff','npxGA','npxGD','ppda_coef','oppda_coef','deep','deep_allowed','xpts','xpts_diff'] #renomeei as colunas

#pd.set_option('max_columns', 24) -> Configura quantas colunas aparecerão no terminal

tabelas_barcelona = df.loc[df['time'] == "Barcelona"] #Separei as temporadas do Barcelona
barcelona2014 = tabelas_barcelona.loc[tabelas_barcelona['temporada'] == 2014 ] #Separei pela temporada que queria
print(barcelona2014.head())