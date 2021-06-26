a = 1
b = 2.2
c = "string"
d = True
n1 = 1; n2 = 2; n3 = complex(n1, n2)
e = ["A", "B", "C", "D"]
f = ("A", 1, "C")
g = range(0, 10)
h = {
    "Nome": "Cristiano Ronaldo",
    "Time": "Juventus",
    "Nacionalidade": "Portugal"
}
i = {1, 1, 2, 3, 4, 4, 5}

print("Tipo: " + str(type(a)))
print("Tipo: " + str(type(b)))
print("Tipo: " + str(type(c)))
print("Tipo: " + str(type(d)))
print("Tipo número complexo: " + str(n3.real))
print("Tipo número complexo: " + str(n3.imag))
print("Tipo: " + str(type(e)))
print("Tipo: " + str(type(e[0])))
print("Tipo: " + str(type(f)))
print("Tipo: " + str(type(g)))
print("Tipo: " + str(type(h)))
print("Tipo: " + str(type(h["Nome"])))
print("Tipo: " + str(type(i)))
print(i) #set

#tipos de dados
#complex números complexos
#type str
#array list 
#tuple
#range - Cria lista
#objeto
#set - Impede repetições