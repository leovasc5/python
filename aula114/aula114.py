import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/l5/python/aula38/planilha2.csv", encoding="UTF-8", sep=",", header=0, 
usecols=["league","season","position","team","matches","wins","draws","loses","scored","missed","pts"], nrows=120)
df.columns = ["liga","temporada","posicao","time","partidas","vitorias","empates","derrotas","gols pro","gols contra","pontos"]

memoria_antiga = df.memory_usage(deep=True)
df_copia = df.copy(deep=True)

df_copia["temporada"] = df_copia["temporada"].astype(np.int16)
df_copia["posicao"] = df_copia["posicao"].astype(np.int8)
df_copia["partidas"] = df_copia["partidas"].astype(np.int8)
df_copia["vitorias"] = df_copia["vitorias"].astype(np.int8)
df_copia["empates"] = df_copia["empates"].astype(np.int8)
df_copia["derrotas"] = df_copia["derrotas"].astype(np.int8)
df_copia["gols pro"] = df_copia["gols pro"].astype(np.int8)
df_copia["gols contra"] = df_copia["gols contra"].astype(np.int8)
df_copia["pontos"] = df_copia["pontos"].astype(np.int8)

print(df_copia.select_dtypes(include=["object", "int8"]).nunique())
print("\n --------------------------- \n")
print("\n ANTIGA")
print(memoria_antiga)

print("\n ATUAL")
print(df_copia.memory_usage(deep=True))

print("\n COMPARAÇÃO")
for i in df.columns:
    value = (df_copia.memory_usage(deep=True)[i]/memoria_antiga[i]) * 100
    value =  100 - value
    print("A memória de \"" + i + "\" foi otimizada em " + str(value) + "%")
