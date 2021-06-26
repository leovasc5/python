def somar(n1, n2):
    res = n1 + n2
    return res

def subtrair(n1, n2):
    res = n1 - n2
    return res

def multiplicar(n1, n2):
    res = n1 * n2
    return res

def dividir(n1, n2):
    res = n1 / n2
    return res
    
soma = somar(10, 23)
subtracao = subtrair(32, 24)
multiplicacao = multiplicar(2, 3)
divisao = dividir(36, 6)

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)

def frase(*n):
    resultado = ""
    for i in n:
        resultado+=i + " "
    print(resultado)

frase("Essa","frase","é","para","teste")

def padrao(estado = "São Paulo"):
    print("Estado: " + estado)

padrao()