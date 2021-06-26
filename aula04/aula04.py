import random

a = 2 #int
b = 4.3 #float
c = 1j #complexo

d = a + b + c
print(type(d))

new_b = int(b)
print(new_b)

new_a = float(a)
print(new_a)

aleatorio = random.randrange(0, 2)
print(aleatorio)

lista_aleatorio = [
    random.randrange(1,11),
    random.randrange(1,11),
    random.randrange(1,11),
    random.randrange(1,11),
    random.randrange(1,11),
]

print(lista_aleatorio)

#conversão lista random import