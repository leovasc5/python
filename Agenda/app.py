from tkinter import *
from tkinter import ttk
from sqlite3 import *
from sqlite3 import Error
import consultar
import inserir


app = Tk()
app.title("Agenda")
app.geometry("500x455")
cfg = ["#f4f4f4", "#000", "#000fff", "#008000"]
app.configure(background=cfg[0])

frameContatos = LabelFrame(app, text="Contatos")
frameContatos.pack(fill="both", expand="yes", padx=10, pady=10)

tv = ttk.Treeview(frameContatos, columns=("Id", "Nome", "Fone"), show="headings")
tv.column("Id", minwidth=0, width=50)
tv.column("Nome", minwidth=0, width=206)
tv.column("Fone", minwidth=0, width=206)
tv.heading("Id", text="ID")
tv.heading("Nome", text="NOME")
tv.heading("Fone", text="FONE")

tv.grid(column=0, row=4, columnspan=3, padx=5, pady=5)

def iniciar_tabela():
    for i in tv.get_children():
        tv.delete(i)

    dados = consultar.todos()

    for (a, b, c) in dados:
        tv.insert("", "end",values=(a, b, c))
    
iniciar_tabela()

def call1(no, t):
    inserir.adicionar(no, t)
    nome.delete(0, END)
    tlf.delete(0, "end")

    for i in tv.get_children():
        tv.delete(i)

    dados = consultar.todos()

    for (a, b, c) in dados:
        tv.insert("", "end",values=(a, b, c))

def call2(query):
    dados = consultar.pesquisar(query)

    for i in tv.get_children():
        tv.delete(i)

    for (a, b, c) in dados:
        tv.insert("", "end",values=(a, b, c))

frameInserir = LabelFrame(app, text="Inserir Novos Contatos")
frameInserir.pack(fill="both", expand="yes", padx=10, pady=10)

lbl1 = Label(frameInserir, text="Nome: ", padx=10, pady=10)
lbl1.pack(side="left")
nome = Entry(frameInserir)
nome.pack(side="left")

lbl2 = Label(frameInserir, text="Telefone: ", padx=10, pady=10)
lbl2.pack(side="left")
tlf = Entry(frameInserir)
tlf.pack(side="left", padx=10)
btn1 = Button(frameInserir, text="Inserir", padx=10, command=lambda:call1(str(nome.get()), str(tlf.get())))
btn1.pack(side="left")

framePesquisar = LabelFrame(app, text="Pesquisar Contatos")
framePesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

lbl3 = Label(framePesquisar, text="Nome: ", padx=10, pady=10)
lbl3.pack(side="left")
pesquisa = Entry(framePesquisar)
pesquisa.pack(side="left", padx=10)
btn2 = Button(framePesquisar, text="Pesquisar", padx=10, command=lambda:call2(str(pesquisa.get())))
btn2.pack(side="left", padx=10)
btn3 = Button(framePesquisar, text="Mostrar Todos", padx=10, command=iniciar_tabela)
btn3.pack(side="left", padx=10)

app.mainloop()