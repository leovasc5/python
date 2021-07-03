def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido!")
    except conexao.Error:
        print(conexao.Error)