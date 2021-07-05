from tkinter import *
import os

def semComando():
    print("Teste")

app = Tk()
app.title("Agenda")
app.geometry("500x350")
cfg = ["#f4f4f4", "#000", "#000fff", "#008000"]
app.configure(background=cfg[0])

barraDeMenus = Menu(app)
menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label="Adicionar", command=semComando)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Deletar", command=semComando)
menuContatos.add_command(label="Lista", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label="Banco de Dados", command=semComando)
barraDeMenus.add_cascade(label="Manutenção", menu=menuManutencao)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Leonardo Vasconcelos", command=semComando)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

app.config(menu=barraDeMenus)
app.mainloop()