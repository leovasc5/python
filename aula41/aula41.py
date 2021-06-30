import pandas as pd

alunosDIC = {
    "Nome": ['Ricardo', 'Pedro', 'Roberto', 'Carlos', 'Ricardo'],
    "Nota": [4, 7, 9, 9.7, 5],
    "Aprovado":['Não', 'Sim', 'Sim', 'Sim', 'Não']
}

alunosDF = pd.DataFrame(alunosDIC)

print(alunosDF["Nome"]) #retorna os dados da coluna específicada

print(alunosDF.loc[[0,2]]) #retorna as linhas de acordo com o filtro desejado
print(alunosDF.loc[0:3]) #retorna as linhas de acordo com o filtro desejado

print(alunosDF.loc[alunosDF['Nome'] == 'Ricardo']) #Retorna as linhas de acordo com o filtro desejado

aprovados = alunosDF.loc[alunosDF['Nota'] >= 6]
print(aprovados)

print("-------------------------")

reprovados = alunosDF.loc[alunosDF['Nota'] < 6]
print(reprovados)