import os
import sqlite3
from sqlite3 import Error
import conexao, inserir, deletar

def menu():
    os.system("cls")
    print("1 - Inserir novo contato")
    print("2 - Excluir contato")
    print("3 - Editar contato")
    print("4 - Ver contato")
    print("5 - Sair")
    print("\n")

opc = 0
while opc != 5:
    menu()
    opc = int(input("Escolha a opção: "))
    
    if opc == 1:
        os.system("cls")
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")

        sql = """INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
        VALUES ('"""+nome+"""','"""+telefone+"""','"""+email+"""')"""
        try:
            inserir.inserir(conexao.con, sql)
            os.system("cls")
            print(nome + " foi adicionado na sua lista de contatos!")
            os.system("pause")
        except:
            print("Algum erro aconteceu :/ Contate o programador")
            os.system("pause")

    elif opc == 2:
        os.system("cls")
        id = input("Digite o ID para deletar: ")
        sql = "DELETE FROM tb_contatos WHERE T_IDCONTATO = '"+id+"'"

        try:
            deletar.deletar(conexao.con, sql)
        except:
            print("Algum erro aconteceu :/ Contate o programador")
            os.system("pause")

    elif opc == 3:
        print("3")
    elif opc == 4:
        print("4")
    elif opc == 5:
        os.system("cls")
        print("Obrigado por me utilizar :) - Fim do Programa")
        opc = 5