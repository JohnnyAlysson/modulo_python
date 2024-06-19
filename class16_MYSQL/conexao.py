import pymysql.cursors


#conexão e cursor
def criarConexao():
    try:
        conexao= pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="biblioteca",
                                cursorclass=pymysql.cursors.DictCursor)
        print("Conexão realizada com sucesso\n")

        return conexao
    except Exception as error:
        print(f"Erro ao conectar-se ao banco! {error}")

def listarTodosLivros():
    try:
        #Criando cursors
        cursor= criarConexao().cursor()
        cursor.execute("SELECT * FROM livros")

        #Fetch

        resultado = cursor.fetchall()
        for livro in resultado:
            print (livro)
    except Exception as error:
        print(f"Erro ao listar todos os livros")

listarTodosLivros()
