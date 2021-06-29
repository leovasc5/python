import json

carros_json = '{"marca":"Jeep","modelo":"Compass","cor":"Cinza"}'

carros = json.loads(carros_json)
#json para dictionary

for x, y in carros.items():
    print(x.capitalize() + " | " + y)

print(type(carros))
print(type(carros_json))

jogador1 = {
    "nome":"Messi",
    "overAll":94,
    "pais":"Argentina",
    "clube":"Barcelona"
}

jogador1 = json.dumps(jogador1)
#dictionary para json

print(type(jogador1))