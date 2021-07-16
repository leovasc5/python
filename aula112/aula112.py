import pandas as pd

df = pd.read_csv("C:/Users/l5/python/aula111/pontuacao_historica_brasileirao.csv", encoding="UTF-8", sep=",")
df_size = df.shape
df_info = df.info()
df_describe = df.describe()
print(df_describe)