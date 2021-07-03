def consultar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        return resultado
    except conexao.Error:
        print(conexao.Error)