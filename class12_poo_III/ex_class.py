class Livro:
    def __init__(self,codigo,titulo,autor,editora):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

    def __repr__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor}"
    

class Editora:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f"Nome: {self.nome} - Email: {self.email}"
    
editora= Editora("Editora infinity LTDA","infinity@gmail.com")
livro = Livro("1", "Codigo limpo", "James", editora)
print(livro)
print(livro.editora)
print(livro.editora.nome)
print(editora)