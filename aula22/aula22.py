class Carro:
    velMax = 0
    ligado = False
    cor = ""

compass = Carro()
compass.velMax = 220
compass.ligado = False
compass.cor = "Cinza Escuro"
print(compass.velMax)
print(compass.ligado)
print(compass.cor)

#if ternario
estado = "sim" if compass.ligado else "não"
print(estado)
renegade = Carro()
territory = Carro()