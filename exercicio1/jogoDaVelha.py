import os
import random
from colorama import Fore, Back, Style

jogarNovamente = ""
jogadas = 0
quemJoga = 2
maxJogadas = 9
vitoria = ""
matriz = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("     1    2    3")
    print("1:    " + matriz[0][0] + " | " + matriz[0][1] + " | "+ matriz[0][2])
    print("    -------------")
    print("2:    " + matriz[1][0] + " | " + matriz[1][1] + " | "+ matriz[1][2])
    print("    -------------")
    print("3:    " + matriz[2][0] + " | " + matriz[2][1] + " | "+ matriz[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

#while True:
    tela()


tela()