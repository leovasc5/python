from tkinter import *
import os
c = os.path.dirname(__file__)
nomeArquivo = c+"\\nomes.txt"


def saveDados():
    arquivo = open(nomeArquivo, "a")
    arquivo.write("Nome........: %s" % nome.get())
    arquivo.write("\nTelefone....: %s" % numero.get())
    arquivo.write("\nEmail.......: %s" % email.get())
    arquivo.write("\nDescrição...: %s" % desc.get("1.0",END))
    arquivo.write("\n\n")
    arquivo.close()
    Label(app, text="Informações salvas com sucesso!", bg=cfg[3], fg=cfg[0], anchor=CENTER).place(x=10, y=280, width=250, height=20)
    nome.delete(0, END)
    numero.delete(0, END)
    email.delete(0, END)
    desc.delete("1.0", END)


app = Tk()
app.title("Aula 59")
app.geometry("500x350")
cfg = ["#f4f4f4", "#000", "#000fff", "#008000"]
app.configure(background=cfg[0])

Label(app, text="Nome:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=10, width=200, height=20)
nome = Entry(app)
nome.place(x=10, y=35, width=100, height=20)

Label(app, text="Telefone:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=60, width=200, height=20)
numero = Entry(app)
numero.place(x=10, y=85, width=100, height=20)

Label(app, text="Email:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=110, width=200, height=20)
email = Entry(app)
email.place(x=10, y=135, width=100, height=20)

Label(app, text="Descrição:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=160, width=200, height=20)
desc = Text(app)
desc.place(x=10, y=185, width=185, height=60)

btn = Button(app, text="Salvar", command=saveDados).place(x=10, y=255, width=60, height=20)

app.mainloop()