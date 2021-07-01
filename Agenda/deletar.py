import conexao

id = input("Digite o ID para deletar: ")
sql = "DELETE FROM tb_contatos WHERE T_IDCONTATO = '"+id+"'"

def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro deletado!")
    except conexao.Error:
        print(conexao.Error)

deletar(conexao.con, sql)