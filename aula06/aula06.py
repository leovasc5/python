nome = "Leonardo Vasconcelos"

result = "Leo" in nome #pesquisa se a string está na variável
print(result)

result = "leo" not in nome #pesquisa se a string não está na variável
print(result)

cidade = "Osasco"
dia = 21
mes = "Junho"
ano = 2021
aluno = "Leonardo"
data = "{}, {} de {} de {}\n\"{}\"" #usa placeholder para preencher os dados depois

print(data.format(cidade, dia, mes, ano, aluno)) #metodo format preenche os espaços do placeholder
