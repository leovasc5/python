import os

carros = []

class Carro:
    nome = ""
    potencia = 0
    velMax = 0
    ligado = False

    def __init__(self, n, p):
        self.nome = self.setNome(n)
        self.potencia = self.setPotencia(p)
        self.velMax =  self.setVelMax(p)
        self.ligado = self.desligar()
    
    def setNome(self, n):
        self.nome = n

    def getNome(self):
        return self.nome

    def setPotencia(self, p):
        self.potencia = p

    def getPotencia(self):
        return self.potencia

    def setVelMax(self, p):
        self.velMax = int(p)
    
    def getVelMax(self):
        return self.velMax

    def getLigado(self):
        return self.ligado

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.desligado = False

    def getDados(self):
        estado = "Ligado" if self.getLigado() else "Desligado" 
        print("Nome: " + self.getNome() + "\nPotência: " + self.getPotencia() + "\nVelocidade Máxima: " + self.getVelMax() + "\nEstado: " + estado)

def menu():
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carros")
    print("7 - Sair")
    print("Quantidade de carros: " + str(len(carros)))
    print(carros)

    option = input("Digite uma opção: ")
    return option

def setCarro():
    os.system("cls") or None
    n = input("Nome do Carro: ")
    p = input("Potência do Carro: ")

    temp = Carro(n, p)
    carros.append(temp)
    print("Carro criado com sucesso!")
    os.system("pause")

def getDados():
    os.system("cls") or None
    n = input("Informe o número do carro: ")
        
    try:
        carros[int(n)].getDados()
    except:
        print("O carro não está na lista")
    os.system("pause")

def excluirCarro():
    os.system("cls") or None
    n = input("informe o número do carro que deseja excluir: ")
    try:
        del carros[int(n)]
    except: 
        print("O carro não está na lista")
    os.system("pause")

def ligarCarro():
    os.system("cls") or None
    n = input("informe o número do carro que deseja ligar: ")
    try:
        carros[int(n)].ligar()
    except: 
        print("O carro não está na lista")
    os.system("pause")

def desligarCarro():
    os.system("cls") or None
    n = input("informe o número do carro que deseja ligar: ")
    try:
        carros[int(n)].desligar()
    except: 
        print("O carro não está na lista")
    os.system("pause")

def listarCarros():
    os.system("cls") or None

    for i in carros:
        print(i.getNome())
    os.system("pause")

retorno = menu()

while retorno != "7":
    if retorno == "1":
        setCarro()
    elif retorno == "2":
        getDados()
    elif retorno == "3":
        excluirCarro()
    elif retorno == "4":
        ligarCarro()        
    elif retorno == "5":
        desligarCarro()
    elif retorno == "6":
        listarCarros()
    else:
        print("Opção invalida!")
    retorno = menu()

    os.system("cls") or None
    print("Programa finalizado!")

    #Não completo