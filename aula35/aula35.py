kmh = [40, 50, 56, 64, 73,79, 85, 96]

#milhas por hora

mph = []
for i in kmh:
    mph.append(i/1.61)

mph2 = map(lambda x: x/1.61, kmh)
print(list(mph2)) #Converto mph2 para list porque o Python entende que o map é um conjunto de dados mto grandes para serem computados