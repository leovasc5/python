import os
os.system('cls') #Apaga as mensagens do terminal do windows

nome = input("Digite seu nome: ")
print("Nome: " + nome)

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor:. "))
res = n1 + n2
print("Olá, " + nome + "! O valor da operação é " + str(res))