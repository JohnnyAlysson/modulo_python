# Crie um classe chamada pessoa com os atributos: nome,
# idade, peso, gênero
class Pessoa():
    def __init__(self,nome:str,idade:int,peso:float,genero:str) :
      
      self.nome =  nome
      self.idade =  idade
      self.peso =  peso
      self.genero =  genero


# Criando as pessoas

pessoa1 = Pessoa("Fulano",80,72.5,"Masculino")
pessoa2 = Pessoa("Sicrana",19,60,"Feminino")
pessoa3 = Pessoa("Xiquim",80,72.5,"Não binário")

lista=[pessoa1,pessoa2,pessoa3]

for pessoa in lista:
   print(f'''
    Nome = {pessoa.nome}
    Idade = {pessoa.idade}
    Peso = {pessoa.peso}
    Gênero = {pessoa.genero}

   ''')
   print("="*30)