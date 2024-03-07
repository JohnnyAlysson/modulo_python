from aluno import Aluno

class Escola:
    def __init__(self,nome,endereço):
        self.nome = nome
        self.endereço = endereço
        self.lista_alunos = [Aluno("Jonas",19,"python",8.2)]

    def adicionarAluno(self,aluno:Aluno):
        self.lista_alunos.append(aluno)

    def editarAluno(self,aluno:Aluno):
        for a in self.lista_alunos:
            if str(a.matricula) == str(aluno.matricula):
                a.nome = aluno.nome
                a.idade = aluno.idade
                a.curso = aluno.curso
                a.nota = aluno.nota
                return True
        return False

    def removerAluno(self,matricula):
        for aluno in self.lista_alunos:
            if str(aluno.matricula) == matricula:
                self.lista_alunos.remove(aluno)
                return True
        return False
        

    def listarAlunos(self):
        return self.lista_alunos
    
if __name__ == "__main__":
    escola= Escola("Infinity", "Rua D")
    aluno = Aluno("Mariana",23, "HTML",10)
    escola.adicionarAluno(aluno)
    print(escola.listarAlunos())
    aluno.nome = "Mariana Oliveira"
    escola.editarAluno(aluno)
    print(escola.listarAlunos())
    escola.removerAluno(aluno.matricula)
    print(escola.listarAlunos())