import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))

from livro.livro_buscar import buscarPorCodigo
from livro.livro_editar import editarLivro
from livro.livro_listar import listarLivros
from livro.deletar_livro import deletarLivro
from livro.livro_registrar import registrarLivro


def menu() -> None:
    while True:
        print("--- Bem vindo ao menu---")
        print(" 1 - Adicionar livro")
        print(" 2 - Editar livro")
        print(" 3 - Deletar livro")
        print(" 4 - Buscar por livro")
        print(" 5 - Listar todos os livros")
        print(" 6 - Sair")

        opcao = input("\nSelecione uma opção:\n")

        if opcao == "1":

            titulo= input("\nQual o título do livro?\n > ").title()

            autor= input("\nQual o nome do autor?\n > ").title()
            registrarLivro(titulo,autor)

        elif opcao== "2":

            codigo= int(input("\nQual o código?\n > "))

            titulo= input("\nQual o titulo?\n > ").title()

            autor= input("\nQual o autor?\n > ").title()

            editarLivro(codigo, titulo, autor)

        elif opcao == "3":
            
            codigo= int(input("\nQual o código?\n > "))
            
            deletarLivro(codigo)

        elif opcao == "4":
            
            codigo= int(input("\nQual o código?\n > "))
            
            print(buscarPorCodigo(codigo))
        
        elif opcao == "5":
            listarLivros()

        elif opcao == "6":
            print("Programa encerrado!")
            break

        else:
            print("\nOpção inválida")

menu()