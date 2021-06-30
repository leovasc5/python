import pandas as pd

df = pd.read_csv('C:/Users/l5/python/aula38/planilha2.csv')

df.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos',
 'xG','xG_diff','npxG','xGA','xGA_diff','npxGA','npxGD','ppda_coef','oppda_coef','deep','deep_allowed','xpts','xpts_diff']

print(df["liga"].value_counts)

pl_dado = df.loc[df["liga"] == "EPL"]
pl_dado = pl_dado.drop_duplicates(subset="temporada") #Exclui duplicidades
print(pl_dado.head())