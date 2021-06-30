import pandas as pd

alunos = {
    "Nome": ['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
    "Nota": [4, 7, 9, 9.7],
    "Aprovado":['Não', 'Sim', 'Sim', 'Sim']
}

dataframe = pd.DataFrame(alunos)
print(dataframe.head())
#Transformou o dicionário em dataframe

objeto1 = pd.Series([1,2,4,6,7,9])
print(objeto1)

matriz = [
    ["1" , "A" , "X"],
    ["2" , "B" , "Y"],
    ["3" , "C" , "Z"]
]

objeto2 = pd.Series(matriz)
print(objeto2)
#Transformou a matriz em dataframe