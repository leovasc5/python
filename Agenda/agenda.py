import os
import sqlite3
from sqlite3 import Error
import conexao

def menu():
    os.system("cls")
    print("1 - Inserir novo contato")
    print("2 - Excluir contato")
    print("3 - Editar contato")
    print("4 - Ver contato")
    print("5 - Sair")

opc = 0
while opc != 5:
    menu()
    opc = int(input("\nEscolha a opção: "))
    
    if opc == 1:
        print("1")
    elif opc == 2:
        print("2")
    elif opc == 3:
        print("3")
    elif opc == 4:
        print("4")
    elif opc == 5:
        os.system("cls")
        print("Obrigado por me utilizar :) - Fim do Programa")
        opc = 5