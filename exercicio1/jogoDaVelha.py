import os
import random
from colorama import Fore, Back, Style

jogarNovamente = ""
jogadas = 0
quemJoga = 2 #1 = CPU | #2 = Jogador
maxJogadas = 9
vitoria = ""
matriz = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def tela():
    global matriz
    global jogadas
    os.system("cls")
    print("     1    2    3")
    print("1:    " + matriz[0][0] + " | " + matriz[0][1] + " | "+ matriz[0][2])
    print("    -------------")
    print("2:    " + matriz[1][0] + " | " + matriz[1][1] + " | "+ matriz[1][2])
    print("    -------------")
    print("3:    " + matriz[2][0] + " | " + matriz[2][1] + " | "+ matriz[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:
        l = int(input("Linha..: "))
        l = l-1

        c = int(input("Coluna.: "))
        c = c-1
        
        try:    
            while matriz[l][c] != " ":
                l = int(input("Linha..: "))
                l = l-1

                c = int(input("Coluna.: "))
                c = c-1

            matriz[l][c] = "X"
            quemJoga = 1
            jogadas+=1
        except:
            print("Espaço inválido!")

def cpuJoga():
    global jogadas
    global maxJogadas
    global quemJoga

    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)

        while matriz [l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        
        matriz[l][c] = "O"
        quemJoga = 2
        jogadas+=1
        
while True:
    tela()
    jogadorJoga()
    cpuJoga()