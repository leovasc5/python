class Carro:
    velMax = 0
    ligado = False
    cor = ""

    def __init__(self, v, l, c):
        self.velMax = v
        self.ligado = l
        self.cor = c

    def showV(self):
        return self.velMax
    
    def showL(self):
        return self.ligado

    def showC(self):
        return self.cor
        
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

compass = Carro(220, False, "Cinza Escuro")
print(compass.showV())
print(compass.showL())
print(compass.showC())
compass.ligar()

renegade = Carro(170, False, "Preto")
territory = Carro(185, False, "Branco")