x = "Olá"
try:
    print(x)
except:
    print("Erro, comunique o programador!")
else:
    print("Tarefa concluída com sucesso!")
finally: 
    print("Fim do programa")

try:
    print(y)
except NameError:
    print("Erro desconhecido")

nome = 1

if not type(nome) is str:
    raise Exception("Somente caractéres!")