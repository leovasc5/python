nome = "Leonardo"
print(nome[0]) #pega a letra de acordo com o indice
print(nome[0:3]) #corta
print("Tamanho: " + str(len(nome))) #pega o tamanho

abc = " ABC DEF GHI "
print(abc)
print(abc.strip()) #tira os espaços
print(abc.lower().strip()) #tudo em minusculo
print(nome.upper()) #tudo em maiusculo
print(nome.replace("Leo", "Leozin ")) #muda o valor desejado

abc = abc.split(" ") #corta e transforma em list
print(abc[2])