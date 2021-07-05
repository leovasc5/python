def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro deletado!")
    except conexao.Error:
        print(conexao.Error)