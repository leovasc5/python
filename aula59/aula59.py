from tkinter import *

app = Tk()
app.title("Aula 59")
app.geometry("500x300")
cfg = ["#f4f4f4", "#000", "#000fff"]
app.configure(background=cfg[0])

Label(app, text="Nome:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=10, width=100, height=20)
nome = Entry(app)
nome.place(x=10, y=35, width=100, height=20)

Label(app, text="Telefone:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=60, width=100, height=20)
numero = Entry(app)
numero.place(x=10, y=85, width=100, height=20)

Label(app, text="Email:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=110, width=100, height=20)
email = Entry(app)
email.place(x=10, y=135, width=100, height=20)

Label(app, text="Descrição:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=160, width=100, height=20)
desc = Text(app)
desc.place(x=10, y=135, width=185, height=60)

app.mainloop()