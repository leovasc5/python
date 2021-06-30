import json 

with open('C:/Users/l5/python/aula34/jogador.json') as f:
    jogador = json.load(f)

for a in jogador:
    print(a)

for b in jogador.items():
    print(b)

for c in jogador.values():
    print(c)