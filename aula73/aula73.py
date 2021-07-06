from tkinter import *

app = Tk()
app.title("Aula 73")
app.geometry("500x475")

def valorEscala():
    print("Valor selecionado: " + str(sc_escala.get()))

lb_valor = Label(app, text="Valor")
lb_valor.pack()

sc_escala = Scale(app, from_=0, to=100, orient=HORIZONTAL, length=400)
sc_escala.set(50)
sc_escala.pack()

btn = Button(app, text="Selecionar valor: ", command=valorEscala)
btn.pack()

app.mainloop()