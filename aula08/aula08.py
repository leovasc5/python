lista = ["Alex", "Bruno", "Carlos", "Deivid", "Ezequiel"]

print(lista[-1]) #imprime a partir do último da lista

lista.append("Fábio")
lista.append("Henrique")

print(str(len(lista)))
lista.remove("Ezequiel")
lista.pop() #remove o último 
del lista[0] #remove por índice
print(lista)

lista2 = ["Fernando", "Gabriel", "Paulo"]

lista+=lista2 #fundi as listas
print(lista)
lista.clear() #apaga a lista