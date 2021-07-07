from tkinter import *
from tkinter import ttk
from tkinter import messagebox

app = Tk()
app.title("Aula 83")
app.geometry("320x350")

def inserir():
    if input1.get() == "" or input2.get() == "" or input3.get() == "":
        messagebox.showerror(title="Erro", message="Alguns campos não estão preenchidos")
        return

    tv.insert("", "end",values=(str(input1.get()), str(input2.get()), str(input3.get())))
    input1.delete(0, END)
    input2.delete(0, END)
    input3.delete(0, END)
    input1.focus()

def deletar():
    try:
        item = tv.selection()[0]
        tv.delete(item)
    except:
        messagebox.showerror(title="Erro", message="Nenhum campo foi selecionado")

def consultar():
    try:
        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado, "values")
        messagebox.showinfo(title="Consulta de "+str(valores[1]), message="ID: "+str(valores[0]+ "\nNome: "+valores[1]+"\nTelefone: "+str(valores[2])))
    except:
        messagebox.showerror(title="Erro", message="Nenhum campo foi selecionado")

lb1 = Label(app, text="Digite o ID: ", padx=5)
lb2 = Label(app, text="Digite o nome:", padx=5)
lb3 = Label(app, text="Digite o número:", padx=5)

input1 = Entry(app)
input2 = Entry(app)
input3 = Entry(app)

lb1.grid(column=0, row=1, sticky=W)
input1.grid(column=1, row=1)

lb2.grid(column=0, row=2, sticky=W)
input2.grid(column=1, row=2)

lb3.grid(column=0, row=3, sticky=W)
input3.grid(column=1, row=3)

tv = ttk.Treeview(app, columns=("Id", "Nome", "Fone"), show="headings")
tv.column("Id", minwidth=0, width=100)
tv.column("Nome", minwidth=0, width=100)
tv.column("Fone", minwidth=0, width=100)
tv.heading("Id", text="ID")
tv.heading("Nome", text="NOME")
tv.heading("Fone", text="FONE")

tv.grid(column=0, row=4, columnspan=3, padx=5, pady=5)

btn_inserir = Button(app, text="Inserir", command=inserir)
btn_deletar = Button(app, text="Deletar", command=deletar)
btn_consultar = Button(app, text="Consultar", command=consultar)

btn_inserir.grid(column=0, row=5, sticky=N, padx=5)
btn_deletar.grid(column=1, row=5, sticky=N, padx=5)
btn_consultar.grid(column=2, row=5, sticky=N, padx=5)

app.mainloop()