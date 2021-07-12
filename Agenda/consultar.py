from tkinter import messagebox
from sqlite3 import *
from sqlite3 import Error
import banco

def todos():
    try:
        query = "SELECT * FROM tb_contatos"
        res = banco.dql(query)
        return res
    except:
        print("Erro ao inserir os dados... Contate o programador")

def pesquisar(query):
    if query != "":
        try:
            query = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+query+"%'"
            res = banco.dql(query)
            return res
        except:
            print("Erro ao consultar os dados... Contate o programador")
    elif query == "":
        messagebox.showerror(title="Erro", message="O campo pesquisa não está preenchido")
    else:
        messagebox.showerror(title="Erro", message="Erro desconhecido. Contate o programador!")