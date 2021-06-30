import pandas as pd

alunosDIC = {
    "Nome": ['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
    "Nota": [4, 7, 9, 9.7],
    "Aprovado":['Não', 'Sim', 'Sim', 'Sim']
}

alunosDF = pd.DataFrame(alunosDIC)
print(alunosDF.head())

print(alunosDF.shape) #Retorna as linhas e colunas do df
print(alunosDF.describe()) #Retorna informações prontas criadas pelo Pandas
