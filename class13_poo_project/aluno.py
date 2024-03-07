from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,nome:str,idade:int,curso:str, nota: float):
        super().__init__(nome,idade)
        self.curso = curso
        self.nota = nota

    def __repr__(self):
        return f"{super().__repr__()}\n curso {self.curso} \n nota: {self.nota}"
    
if __name__ == "__main__":
    print(Aluno("Jonas", 20, "Python",9.95))