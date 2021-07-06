from tkinter import *

app = Tk()
app.title("Aula 75")
app.geometry("300x300")

def showEsporte():
    print("Esporte: " + str(lb_esportes.get(ACTIVE)))
    btn_esporte.configure(text="Escolhido")
    btn_esporte.configure(state=DISABLED)
    lb_esportes.configure(state=DISABLED)

listaEsportes = ["Futebol", "Vôlei", "Basquete"]
lb_esportes = Listbox(app)

for esporte in listaEsportes:
    lb_esportes.insert(END, esporte)

lb_esportes.pack()

btn_esporte = Button(app, text="Selecionar", command=showEsporte)
btn_esporte.pack()

app.mainloop()