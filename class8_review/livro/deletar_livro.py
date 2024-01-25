import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))
from repositorio.livro_repositorio import livro_repositorio
from livro.livro_buscar import buscarPorCodigo

def deletarLivro(codigo:int) -> None:
    livro = buscarPorCodigo(codigo)
    if livro:
        livro_repositorio.remove(livro)
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado!")

if __name__ == "__main__":
    deletarLivro(1)
    buscarPorCodigo(1)