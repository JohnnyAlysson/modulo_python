from datetime import datetime
import random

class Banco:
    def __init__(self) -> None:
        pass

    def criarConta(self,n_conta,nome):
        conrrentistas[f"{n_conta}"] = [nome,0]

    def deposito(self,dinheiro:float,):
        self.saldo += dinheiro
        time_now = str(datetime.now())
        self.extrato.update({time_now : f"+ {dinheiro}" })

    
    def saque (self,valor_saque:float,):
        if self.saldo < valor_saque:
            print("Voce nao possui saldo suficiente")
        else:
            saldo -=valor_saque
            time_now = str(datetime.now())
            self.extrato.update({time_now : f"- {valor_saque}" })
    
    def consultarSaldo(self):
        print(f"Seu saldo atual e:{self.saldo}")

    def consultarExtrato(self):
        for i in self.extrato:
            print(f'''
                Horario: {i}
                Transacao: {self.extrato.get(i)}                 
''')
class Conta():

    def __init__(self,nDaConta,nome,saldo,):
        self.nDaConta = nDaConta
        self.nome = nome
        self.saldo = saldo
        self.extrato = []

    def get_nDaConta(self):
        return self.nDaConta

    def set_nDaConta(self, value):
        self.nDaConta = value

    def get_nome(self):
        return self.nome

    def set_nome(self, value):
        self.nome = value

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, value):
        self.saldo = value

    def get_extrato(self):
        return self.extrato

    def set_extrato(self, value):
        self.extrato = value


    
    
    
################# UI #########################
# while True:
#     choice_conta = str ('''
#     Seja bem vindo ao banco bradestautander
#     digite 1 se voce e correntista
#     digite 2 para abrir uma nova conta
#     digite 0 para sair             
# ''')
#     if choice_conta == "1":
#         numero_conta = input("Por gentileza informe o numero da conta:")
#         while True:
#             choice = str(input('''
#             Qual operacao voce deseja realizar:
#                 1 - Deposito;
#                 2 - Saque;
#                 3 - Consultar Saldo;
#                 4 - Verificar Extrato;
#                 0 - Sair.
#         '''))
#             if choice == "1":
#                 pass
#             elif choice == "0":
#                 print("Operacao encerrada")
#                 break
#             else:
#                 print("Comando invalido")
    
#     elif choice_conta == "2":
#         while True:
#             n_conta_nova = random.randint(1,100)
#             if n_conta_nova in conrrentistas.keys():
#                 n_conta_nova = random.randint(1,100)
#             else:
#                 break

#         nome= str(input("Digite seu nome:"))
#         Conta.criarConta(n_conta_nova,nome)






    












# # teste extrato:
# saldo = 0
# extrato = {}
# time_now = str(datetime.now())

# deposito1 = 200
# saldo += deposito1
# extrato.update({time_now : str(deposito1)})


# sleep(5)
# time_now = str(datetime.now())
# deposito2 = 500
# saldo += deposito2
# extrato.update({time_now : str(deposito2)})
#print(saldo,extrato)

