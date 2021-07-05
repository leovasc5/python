from tkinter import *
import os, banco


def saveDados():
    if (tb_nome.get() != "") & (tb_numero.get() != "") & (tb_email.get() != "") & (tb_desc.get("1.0",'end-1c') != ""):
        nome = tb_nome.get()
        numero = tb_numero.get()
        email = tb_email.get()
        desc = tb_desc.get("1.0",'end-1c')
        query = """INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_DESC)
                    VALUES ('"""+nome+"""', '"""+numero+"""', '"""+email+"""', '"""+desc+"""')"""
        banco.dml(query)

        Label(app, text="Informações salvas com sucesso!", bg=cfg[3], fg=cfg[0], anchor=CENTER).place(x=10, y=280, width=250, height=20)
        tb_nome.delete(0, END)
        tb_numero.delete(0, END)
        tb_email.delete(0, END)
        tb_desc.delete("1.0", END)
    else:
        print("Erro")


app = Tk()
app.title("Aula 59")
app.geometry("500x350")
cfg = ["#f4f4f4", "#000", "#000fff", "#008000"]
app.configure(background=cfg[0])

Label(app, text="Nome:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=10, width=200, height=20)
tb_nome = Entry(app)
tb_nome.place(x=10, y=35, width=100, height=20)

Label(app, text="Telefone:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=60, width=200, height=20)
tb_numero = Entry(app)
tb_numero.place(x=10, y=85, width=100, height=20)

Label(app, text="Email:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=110, width=200, height=20)
tb_email = Entry(app)
tb_email.place(x=10, y=135, width=100, height=20)

Label(app, text="Descrição:", bg=cfg[0], fg=cfg[1], anchor=W).place(x=10, y=160, width=200, height=20)
tb_desc = Text(app)
tb_desc.place(x=10, y=185, width=185, height=60)

btn = Button(app, text="Salvar", command=saveDados).place(x=10, y=255, width=60, height=20)

app.mainloop()