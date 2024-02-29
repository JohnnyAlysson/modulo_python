class Veiculo :
    def __init__(self,marca,modelo,cor):
        self.marca = marca 
        self.modelo = modelo 
        self.cor = cor
        self.ligado = False
        self.velocidadeAtual = 0 

    def ligar(self):
        self.ligado = True
        print("Veiculo ligado")

    def desligar(self):
        self.ligado = False
        print("Veiculo desligado")

    def acelerar(self):
        pass

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, numeroPortas):
        super().__init__(marca, modelo, cor)
        self.numeroPortas = numeroPortas
    
    def acelerar(self):
        if self.ligado:
            self.velocidadeAtual += 25
            print(f" Aumentando velocidade: {self.velocidadeAtual} km/h")
            return
        print("O Veiculo está desligado")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor,cilindrada):
        super().__init__(marca, modelo, cor)
        self.cilindrada = cilindrada
    
    def acelerar(self):
        if self.ligado:
            self.velocidadeAtual += 35
            print(f" Aumentando velocidade: {self.velocidadeAtual} km/h")
            return
        print("O Veiculo está desligado")



carro = Carro("Fiat","Uno","Vermelho",4)
carro.ligar()
carro.acelerar()




moto = Moto("Honda","Cb","Vermelho",300)
moto.ligar()
moto.acelerar()
