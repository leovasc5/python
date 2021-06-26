objeto = {
    "Fabricante":"Jeep",
    "Modelo":"Compass",
    "Ano":2022,
    "Cor":"Azul meia-noite"
}

print(str(len(objeto)))

objeto["Câmbio"] = "Automático"

for x in objeto:
    print(str(x) + ": " + str(objeto[x]))

print("\n")
objeto.pop("Câmbio")
del objeto["Ano"]

for x in objeto:
    print(str(x) + ": " + str(objeto[x]))

objeto.clear()
print(objeto)

superObjeto = {
    "Obj1" :{
        "A" : "a",
        "B" : "b",
        "C" : "c"
    },

    "Obj2" :{
        "E" : "e",
        "F" : "f",
        "G" : "g"
    },

    "Obj3" :{
        "H" : "h",
        "I" : "i",
        "J" : "j"
    }
}

print("\n")
print(superObjeto)

abc = {
    "abc" : superObjeto["Obj1"],
    "efg" : superObjeto["Obj2"],
    "hij" : superObjeto["Obj3"]
}

print("\n")
print(abc)