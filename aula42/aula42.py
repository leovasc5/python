import pandas as pd

alunosDIC = {
    "Nome": ['Ricardo', 'Pedro', 'Roberto', 'Carlos', 'Ricardo'],
    "Nota": [4, 7, 9, 9.7, 5],
    "Aprovado":['Não', 'Sim', 'Sim', 'Sim', 'Não']
}

alunosDF = pd.DataFrame(alunosDIC)

aprovados = alunosDF.loc[alunosDF['Nota'] >= 6]

novoDF = 