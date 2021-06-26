import os

i = 0
while i < 10:
    print(i+1)
    i+=1
    if i == 5:
        print("\nFim do while!\n")
        break

players = ["Cr7", "Messi", "Neymar"]

j=0
while j < len(players):
    print(players[j])
    j+=1

k=0
times = []
time = input("Digite o nome do novo time: ")
while time != "stop":
    times.append(time)
    time = input("Digite o nome do novo time: ")

os.system('cls')

for h in times:
    print(h)