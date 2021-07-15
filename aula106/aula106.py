import pandas as pd

estados = pd.Series(["ES", "MG", "RJ", "SP"])
pibs = pd.Series([137.0, 614.8, 758.8, 2210.5])
dados = zip(estados, pibs)

var_index =[*"ABCD"]
var_columns = ["Estado", "PIB"]

df = pd.DataFrame(data=dados, index=var_index, columns=var_columns)
print(df)

lucros = pd.Series([1024.50, 500.06, 1000.32, 2789.80])
gastos = pd.Series([540.89, 1025.07, 124.00, 87.00])
dados2 = zip(lucros, gastos)
df2 = pd.DataFrame(data=dados2, index=pd.date_range("07/01/2021", periods=4), columns=["Lucro", "Gasto"])
print(df2)