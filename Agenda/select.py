import conexao

nome = input("Digite o nome que deseja pesquisar: ")

sql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO = '"+nome+"'"

def consultar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        return resultado
    except conexao.Error:
        print(conexao.Error)

res = consultar(conexao.con, sql)

for i in res:
        for j in i:
            print(j)