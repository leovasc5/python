import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho = "C:\\Users\\l5\\python\\Agenda\\banco\\agenda.db"
    con = None
    try: 
        con = sqlite3.connect(caminho)
    except Error:
        print(Error)
    return con

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

sql = """INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
        VALUES ('"""+nome+"""','"""+telefone+"""','"""+email+"""')"""

def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido!")
    except Error:
        print(Error)
con = ConexaoBanco()
inserir(con, sql)