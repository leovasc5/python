from tkinter import *

app = Tk()
app.title("Aula 76")
app.geometry("300x300")

def showEsporte():
    print("Esporte: " + str(lb_esportes.get(ACTIVE)))

def addEsporte():
    lb_esportes.insert(END, adicionar.get())

listaEsportes = ["Futebol", "Vôlei", "Basquete"]
lb_esportes = Listbox(app)

for esporte in listaEsportes:
    lb_esportes.insert(END, esporte)

lb_esportes.pack()

btn_esporte = Button(app, text="Selecionar", command=showEsporte)
btn_esporte.pack()

adicionar = Entry(app)
adicionar.pack()

btn_inserir =  Button(app, text="Adicionar esporte", command=addEsporte)
btn_inserir.pack()

app.mainloop()