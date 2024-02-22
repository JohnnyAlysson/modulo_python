import uuid
class Aluno:
    def __init__(self, nome , curso):
        self.nomeAluno = nome
        self. cursoAluno = curso
        self.matricula = str(uuid.uuid4())
        self.qtdFaltas = 0

    def atribuirFalta(self):
        self.qtdFaltas += 1

alunosMatriculados =[]

aluno1=Aluno("Jonas", "Python")
aluno2=Aluno("Letícia", "Java")
print(aluno1.nomeAluno,aluno1.cursoAluno)

aluno1.nomeAluno="Jonas Lopes"
print(aluno1.nomeAluno,aluno1.matricula)

aluno1.atribuirFalta()
aluno1.atribuirFalta()
aluno2.atribuirFalta()

alunosMatriculados.append(aluno1)
alunosMatriculados.append(aluno2)

print("---  DADOS DOS ALUNOS ---")
for aluno in alunosMatriculados:
    print("--- DADOS DOS ALUNOS ---")
for aluno in alunosMatriculados:
    print(f"Matricula: {aluno.matricula}")
    print(f"Nome: {aluno.nomeAluno}") 
    print(f"Curso: {aluno.cursoAluno}")
    print(f"Quantidade de faltas: {aluno.qtdFaltas}") 
    print("*" * 50)  



