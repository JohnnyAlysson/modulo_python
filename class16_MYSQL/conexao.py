import pymysql.cursors
import cowsay


#conexão e cursor
def criarConexao():
    try:
        conexao= pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="biblioteca",
                                cursorclass=pymysql.cursors.DictCursor)
        # mensagem = "Conexão realizada com sucesso\n"
        # print(cowsay.get_output_string('cow', mensagem))
        return conexao
    except Exception as error:
        print(f"Erro ao conectar-se ao banco! {error}")

def listarTodosLivros():
    try:
        #Criando cursos
       
        cursor= criarConexao().cursor()
        cursor.execute("SELECT * FROM livros")

        #Fetch

        resultado = cursor.fetchall()
        for livro in resultado:
            print (livro)
    except Exception as error:
        print(f"Erro ao listar todos os livros")

listarTodosLivros()
