# import banco/
import os
os.system("python ../banco/conexao.py")

id = input("Digite o ID para atualizar: ")
nome = input("Digite o nome para atualizar: ")
telefone = input("Digite o telefone para atualizar: ")
email = input("Digite o email para atualizar: ")

sql = "UPDATE tb_contatos SET T_NOMECONTATO = '"+nome+"', T_TELEFONECONTATO = '"+telefone+"', T_EMAILCONTATO = '"+email+"' WHERE T_IDCONTATO = '"+id+"'" 

def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro atualizado!")
    except conexao.Error:
        print(conexao.Error)

atualizar(os.con, sql)