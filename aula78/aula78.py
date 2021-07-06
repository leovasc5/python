from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Aula 77")
app.geometry("300x300")

nb = ttk.Notebook(app)
nb.place(x=0 ,y=0, width=300, height=300)

tb1 = Frame(nb)
tb2 = Frame(nb)

nb.add(tb1, text="Primeiro")
nb.add(tb2, text="Segundo")

lb1 = Label(tb1, text="Sou a primeira parte!")
lb1.pack()

lb2 = Label(tb2, text="Sou a segunda parte!")
lb2.pack()

app.mainloop()