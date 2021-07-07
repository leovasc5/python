from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD

app = Tk()
app.title("Aula 80")
app.geometry("300x300")

lb1 = Label(app, text="Leonardo Vasconcelos", font="bold")
lb2 = Label(app, text="Digite o seu nome")
lb3 = Label(app, text="Digite sua idade")

input1 = Entry(app)
input2 = Entry(app)

btn1 = Button(app, text="YouTube")

lb1.grid(column=0, row=0, columnspan=2)

lb2.grid(column=0, row=1, sticky=W)
input1.grid(column=1, row=1)

lb3.grid(column=0, row=2, sticky=W)
input2.grid(column=1, row=2)

app.mainloop()