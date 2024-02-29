
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

class Livro:
    def __init__(self, titulo, autor, biblioteca):
        self.titulo = titulo 
        self.autor = autor
        self.biblioteca = biblioteca
    
    def __repr__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor}"

biblioteca = Biblioteca("Biblio Infinity")
livro1 = Livro("Harry potter", "JK Rolling", biblioteca)
livro2 = Livro("Codigo Limpo", "James", biblioteca)
biblioteca.livros.append(livro1)
biblioteca.livros.append(livro2)
print(biblioteca.livros)