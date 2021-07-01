import re
texto = "Olá_mundo!_Eu_sou_Leonardo_Vasconcelos"

res = re.sub("_", " ", texto) #Substitue o caractéres configurado no parâmetro
print(res)
