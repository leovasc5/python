import re
import os

caminho = "C:/Users/l5/python/aula57/teste.txt"

if os.path.exists(caminho):
    print("Arquivo existente!")
    res = print(input("Você deseja excluir? [s][n] :"))
    if res == "s":
        os.remove(caminho)
    elif res == "n":
        "Fim do programa"
    else:
        "Opção incorreta!\n Fim do programa"
else:
    res2 = print(input("O arquivo não existe... Você deseja criá-lo? [s][n] :"))
    if res2 == "s":
        file = open(caminho, "x")
        print("Arquivo criado!")
    elif res2 == "n":
        print("Fim do programa")
    else:
        print("Fim do programa")