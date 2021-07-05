import sqlite3
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp + "\\banco\\agenda61.db"

def ConexaoBanco():
    con = None
    try:
        con = sqlite3.connect(nomeBanco)
    except Error:
        print(Error)
    return con

def dql(query): #select
    con = ConexaoBanco()
    c = con.cursor()
    c.execute(query)
    res = c.fetchall()
    con.close()
    return res

def dml(query): #insert, update, delete
    
        con = ConexaoBanco()
        c = con.cursor()
        c.execute(query)
        con.commit()
        con.close()
    
        #print(Error)