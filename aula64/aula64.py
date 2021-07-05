from tkinter import *

app = Tk()
app.title("Aula 64")
app.geometry("500x300")

def showEsporte():
   print(vesporte.get())
       
esportes_lista = ["Futebol", "Vôlei", "Basquete"]
vesporte = StringVar()
vesporte.set("Selecione uma opção")

esportes = Label(app, text="Esportes")
esportes.pack()

op_esportes = OptionMenu(app, vesporte, *esportes_lista)
op_esportes.pack()

btn_esporte =  Button(app, text="Esporte Selecionado", command=showEsporte)
btn_esporte.pack()

app.mainloop()