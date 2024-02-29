# 1. Crie uma classe chamada Cliente com os seguintes atributos
# - id: int ou str 
# - nome: str
# - cpf: str
# - endereco: Endereco

# 2. Crie uma classe chamada Endereco com os atributos
# - rua: str
# - bairro: str
# - cep: str
# - cidade: str
# - estado: str
# - numero: str

from random import randint

class Cliente:
    def __init__(self,nome:str,cpf:str):
        self.id = randint(1,1000)
        self.nome=nome
        self.cpf=cpf
        self.endereco=[]

    def cadastrarEndereco(self,endereco):
        self.endereco.append(endereco)
        print("Endereço cadastrado com sucesso!")

    def __repr__(self):
        return f"Nome: {self.nome}, Cpf: {self.cpf}, Endereços: {self.endereco}"
    
class Endereco:
    def __init__(self,rua:str,bairro:str,cep:str,cidade:str,estado:str,numero:str,tipo:str):
        self.rua = rua
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.tipo = tipo

    def __repr__(self):
        return f"Logradouro: {self.rua}, Numero {self.numero}, Bairro: {self.bairro}, Cep: {self.cep}, Cidade: {self.cidade}, Estado: {self.estado}, tipo: {self.tipo} "

cliente = Cliente("fulano","999.999.999-99")

enderecoComercial = Endereco("Rua das aboboras","Jenipapo","xxxxx-xxx","Tamagandapio","Acre","Brasil", "Comercial")
enderecoResidencial = Endereco("Rua dos abacates","Hadouken","00000-000","xingú","MG","Brazil", "residencial")

cliente.cadastrarEndereco(enderecoComercial)
cliente.cadastrarEndereco(enderecoResidencial)

print(cliente)