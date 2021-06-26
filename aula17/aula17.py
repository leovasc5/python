import random
import os

numero = random.randrange(1, 6)
tentativas = 1

n1 = int(input("Tente adivinhar o número: "))
if n1 == numero:
    print("Você acertou!\nTentativas: 1")
elif (n1-1) == numero or (n1+1) == numero:
    print("Quente")
else:
    print("Frio")

while n1 != numero:
    n1 = int(input("Tente adivinhar o número: "))
    tentativas+=1
    if n1 == numero:
        print("Você acertou!\nTentativas: " + str(tentativas))
    elif (n1-1) == numero or (n1+1) == numero:
        print("Quente")
    else:
        print("Frio")
