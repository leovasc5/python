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

con = ConexaoBanco()