# Crie um classe chamada cachorro com os atributos:
# nome, raça, idade

class Cachoro():

    def __init__(self,nome,raça,idade) :
        self.nome = nome
        self.raça = raça
        self.idade = idade

    def latir(self):
        print(f" {self.nome} : Au Au")

    def pegarBola(self):
        print(f" {self.nome} pegou a bolinha:")


cachorro1 = Cachoro("Fuxico","SRD","5")
cachorro2 = Cachoro("Lulu","Akita","3")

cachorro1.latir()
