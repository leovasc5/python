matriz = [
    ["Modelo", "HRV", "A"],
    ["Fabricante", "Honda", "B"],
    ["Ano", 2016, "C"]
]

print(str(len(matriz[1])))

for i, j, k in matriz:
    print("Linha: " + str(i) + "\nValor: " + str(j) + "\nCódigo: " + str(k))