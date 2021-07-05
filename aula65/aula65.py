from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("Aula 64")
app.geometry("500x300")

def showMessage(tipo, msg):
    if tipo == "info":
        messagebox.showinfo(title="App", message=msg)
    elif tipo == "warning":
        messagebox.showwarning(title="App", message=msg)
    elif tipo == "error":
        messagebox.showerror(title="Error", message=msg)
    else:
        print("Erro")

lista_options = ["info", "warning", "error"]

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