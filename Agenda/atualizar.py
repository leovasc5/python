def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro atualizado!")
    except conexao.Error:
        print(conexao.Error)