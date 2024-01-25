import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))
from repositorio.livro_repositorio import livro_repositorio
from livro.livro_buscar import buscarPorCodigo

def editarLivro(codigo : int, titulo: str, autor: str) -> None:
    livro= buscarPorCodigo(codigo)
    if livro:
        livro['titulo'] = titulo
        livro['autor'] = autor
        print('Dados Alterados com sucesso!')
    else:
        print("livro não encontrado")


if __name__ == "__main__":
    editarLivro(1,"Reliquias da morte","J K Rowling")

    print(buscarPorCodigo(1))
