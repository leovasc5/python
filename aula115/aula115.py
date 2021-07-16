from numpy.lib.type_check import real
import pandas as pd
import numpy as np

lucros = pd.Series([1024.50, 500.06, 1000.32, 2789.80, None, 1821.50])
gastos = pd.Series([540.89, 1025.07, 124.00, 87.00, 1025.67, None])
dados = zip(lucros, gastos)
df = pd.DataFrame(data=dados, index=pd.date_range("07/01/2021", periods=6), columns=["Lucro", "Gasto"])

lucros = pd.Series([1024.50, 500.06, "-", 2789.80, 1000.32, 1821.50])
gastos = pd.Series([540.89, 1025.07, 124.00, "-", 1025.67, 87.00])
dados = zip(lucros, gastos)
df2 = pd.DataFrame(data=dados, index=pd.date_range("07/01/2021", periods=6), columns=["Lucro", "Gasto"])

novaSeriesLucro = []
for i in df["Lucro"]:
    if np.isnan(i):
        novaSeriesLucro.append("Não Informado")
    else:
        novaSeriesLucro.append(i)
df["Lucro"] = novaSeriesLucro

novaSeriesGasto = []
for j in df["Gasto"]:
    if np.isnan(j):
        novaSeriesGasto.append("Não Informado")
    else:
        novaSeriesGasto.append(j)
df["Gasto"] = novaSeriesGasto

df2["Lucro"] = df2["Lucro"].replace("-", 0)
df2["Gasto"] = df2["Gasto"].replace("-", 0)

# print(df)
print(df2)