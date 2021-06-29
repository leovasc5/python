import datetime

data = datetime.datetime.now()
nasc = datetime.datetime(2003,11,2,16,44,40)

print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))
print(str(nasc.day) + "/" + str(nasc.month) + "/" + str(nasc.year))

print(nasc.strftime("%A")) #Dia da Semana
print(nasc.strftime("%W")) #Semana em formato de número
print(nasc.strftime("%w")) #Dia em formato de número
print(nasc.strftime("%d")) #Dia do mês
print(nasc.strftime("%b")) #Mês abreviado
print(nasc.strftime("%B")) #Mês string
print(nasc.strftime("%m")) #Número do mês
print(nasc.strftime("%y")) #Ano de 2 digitos
print(nasc.strftime("%Y")) #Ano com 4 digitos
print(nasc.strftime("%H")) #Horário com 2 digitos
print(nasc.strftime("%I")) #Horário AM
print(nasc.strftime("%p")) #Parte do dia
print(nasc.strftime("%M")) #Minutos
print(nasc.strftime("%j")) #Dia do ano 001 -> 365