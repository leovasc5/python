import json

#indent -> indenta de acordo com a quantidade de caractéres passadas
#separators -> troca o separador de acordo com o caractére passado
#sort_keys -> organiza os itens em ordem alfabética

carros_dictionary = {
    "marca":"Jeep",
    "modelo":"Compass",
    "cor":"Cinza"
}

carros = json.dumps(carros_dictionary, indent=4, separators=(":","="), sort_keys=True)
print(carros) 
#dictionary -> objeto json

marcas_list=["Jeep", "Volkswagem", "Volvo", "Nissan", "Hyundai"]

marcas = json.dumps(marcas_list)
print(marcas)
#list -> array json

modelos_tupla = ("Compass", "Renegade", "Territory", "Kicks", "T-Cross")
modelos = json.dumps(modelos_tupla)
#tupla -> array json

