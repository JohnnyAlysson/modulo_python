# Crie uma classe Empresa que permita gerenciar
# funcionários. Os funcionários devem ter informações
# como nome, cargo e salário. A empresa deve ser capaz
# de adicionar, remover e listar funcionários.

class Empresa:
    def __init__(self):
        self.funcionarios=[]
        pass

    def adicionar(self,funcionario):
        self.funcionarios.append(funcionario)

    def remover(self,nome):
        for funcionario in self.funcionarios:
            if nome == funcionario.nome:
                self.funcionarios.remove(funcionario)
            else:
                pass
        

    def listar(self):
        print("################### LISTA DE FUNCIONÁRIOS ###################")
        for funcionario in self.funcinarios:
            print(f'''
                
                Nome: {funcionario.nome}
                cargo: {funcionario.cargo}
                salario: R$ {funcionario.salario}

                ''')



class funcionario:
    def __init__(self,nome,cargo,salario):
        self.nome=nome
        self.cargo=cargo
        self.salario=salario
        

# controlador:
print("Seja bem vindo, iniciando programa")
while True:
    choice = input('''
        Digite uma opção:
        1 - Adicionar Funcionário
        2 - Remover Funcionário
        3 - Listar Funcionários
        0 - Finalizar programa 
        ''')
    
    if choice == "1":
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = input("Digite o salário do funcionário: ")
        pessoa = funcionario(nome,cargo,salario)
        Empresa.adicionar(Empresa,pessoa)
        print("Funcionário adicionado com sucesso")

    elif choice == "2":
        nome= input("Digite o nome do funcionário")
        Empresa.remover(nome)
        print("Funcionário removido com sucesso")
        
    elif choice == "3":
        Empresa.listar()
        
    elif choice == "0":
        break
    else:
        print("Comando Inválido, tente novamente")

print("Fim de programa")