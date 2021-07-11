from tkinter import messagebox
from sqlite3 import *
from sqlite3 import Error
import banco

def adicionar(nome, tlf):
    if nome != "" and tlf != "":
        try:
            query = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO) VALUES('"+nome+"', '"+tlf+"')"
            banco.dml(query)
        except:
            print("Erro ao inserir os dados... Contate o programador")
    elif nome == "" and tlf == "":
        messagebox.showerror(title="Erro", message="Os campos não estão preenchidos")
    elif nome == "" and tlf != "":
        messagebox.showerror(title="Erro", message="O campo \"Nome\" não está preenchido")
    elif nome != "" and tlf == "":
        messagebox.showerror(title="Erro", message="O campo \"Telefone\" não está preenchido")
    else:
        messagebox.showerror(title="Erro", message="Erro inesperado, contate o programador")