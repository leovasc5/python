import re
texto = "Olá_mundo!_Eu_sou_Leonardo_Vasconcelos"

while True:
    search = input("Pesquisar: ")
    res = re.findall(search.lower(), texto.lower())
    print("\nResultados:")

    if len(res) == 0:
        print("Não foi encontrado nada\n")
    else:
        for i in res:
            print(i)
            print("Tamanho: " +str(len(i)) + "\n")