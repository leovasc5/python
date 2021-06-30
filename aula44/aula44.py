import pandas as pd

df = pd.read_csv('C:/Users/l5/python/aula38/planilha2.csv')

df.columns = ['liga','temporada','posicao','time','partidas','vitorias','empates','derrotas','gols pro','gols contra','pontos',
 'xG','xG_diff','npxG','xGA','xGA_diff','npxGA','npxGD','ppda_coef','oppda_coef','deep','deep_allowed','xpts','xpts_diff']

excluir_colunas = ['xG','xG_diff','npxG','xGA','xGA_diff','npxGA','npxGD','ppda_coef','oppda_coef','deep','deep_allowed','xpts','xpts_diff']

for i in excluir_colunas:
    df.drop(i, axis=1, inplace=True)

print(df.head())