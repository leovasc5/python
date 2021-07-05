from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("Aula 64")
app.geometry("500x300")

def showMessage(tipo, msg):
    if tipo == "askyesno":
        res = messagebox.askyesno(title="App", message=msg)
        print(res)
    elif tipo == "askokcancel":
        res = messagebox.askokcancel(title="App", message=msg)
        print(res)
    elif tipo == "askretrycancel":
        res = messagebox.askretrycancel(title="Error", message=msg)
        print(res)
    elif tipo == "askyescancel":
        res = messagebox.askyescancel(title="Error", message=msg)
        print(res)
    elif tipo == "askyesnocancel":
        res = messagebox.askyesnocancel(title="Error", message=msg)
        print(res)
    else:
        print("Erro")

lista_options = ["askyesno", "askokcancel", "askretrycancel", "askyescancel", "askyesnocancel"]

Label(app, text="Tipo de caixa")
vtipo = StringVar()
vtipo.set("Selecione uma opção")

txtTipos = Label(app, text="Tipos de caixa")
txtTipos.pack()

op_tipos = OptionMenu(app, vtipo, *lista_options).pack()

Label(app, text = "Digite a mensagem").pack()
msg = Entry(app)
msg.pack()

Button(app, text="Criar caixa", command=lambda:showMessage(vtipo.get(), msg.get())).pack()

app.mainloop()