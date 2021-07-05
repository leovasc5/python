from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("Aula 68")
app.geometry("500x475")

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

fr_quadro1 = Frame(app, borderwidth = 1, relief="solid")
fr_quadro1.place(x=10, y=10, width=300, height=200)

Label(fr_quadro1, text="Tipo de caixa")
vtipo = StringVar()
vtipo.set("Selecione uma opção")


txtTipos = Label(fr_quadro1, text="Tipos de caixa")
txtTipos.pack()

op_tipos = OptionMenu(fr_quadro1, vtipo, *lista_options).pack()

Label(fr_quadro1, text = "Digite a mensagem").pack()
msg = Entry(fr_quadro1)
msg.pack()

Button(fr_quadro1, text="Criar caixa", command=lambda:showMessage(vtipo.get(), msg.get())).pack()

fr_quadro2 = Frame(app, borderwidth = 1, relief="solid", bg="#041E42")
fr_quadro2.place(x=10, y=250, width=300, height=200)

lbl1 = Label(fr_quadro2, text="Leonardo Vasconcelos", fg="#f4f4f4", bg="#041E42", font=("Arial", 15))
lbl1.pack(fill=X, expand=True)


app.mainloop()