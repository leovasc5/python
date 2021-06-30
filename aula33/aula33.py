import json

jogador_j = '{"nome":"Bruno","time":"aviadores","vivo": "True","energia": 100,"mochila": ["pederneira", "corda", "linha", "arame"],"aeronaves": [{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'
jogador = json.loads(jogador_j)

for c in jogador:
    print(c)

for b in jogador.items():
    print(b)

for c in jogador.values():
    print(c)

for d in jogador["mochila"]:
    print(d)

for e in jogador["aeronaves"]:
    print(e["tipo"] + " Habilidade: " + str(e["habilidade"]))