class Carro():
	#atributos
	#cor,modelo,ano,marca
	def __init__(self,cor,modelo,ano,marca): #Construtor
		self.cor = cor
		self.modelo = modelo
		self.ano = ano
		self.marca = marca
	#métodos
	def ligar(self):
		print(f"O {self.modelo} está ligado !!")



###### fora da classe ###########

carro1 = Carro("prata","hilux","2020","Toyota")
carro2 = Carro("vermelho","moby","2016","Fiat")
print(carro1.marca)
carro2.ligar()
