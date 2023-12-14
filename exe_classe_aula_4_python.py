#Anotações da aula:
# dicionario={
#     "nome":"ana",
#     "idade": 30,
#     "altura":1.63,
#     "legal?":True,
#     "habilidades":["Ler","Cozinhar"]

# }
# print(dicionario["habilidades"][1])         # Imprimir do dicionario o valor referente a habilidade na posição do index 1 ou seja cozinhar

# dicionario["idade"] = 31
# dicionario["peso"] = 70                     # Adicionei uma nova chave que não existia

# for x,y in dicionario.items():
#     print(x," = ",y)

# print("\n")
# for i in dicionario:
#     print(i," = ",dicionario.get(i))



### Exercicios slide: ###
# # 01. Crie um dicionário d e coloque nele seus dados: nome, idade, telefone, endereço;
# d={
#     "nome":"johnny",
#     "idade":"27",
#     "telefone":"8599957543",
#     "endereço":"rua dos caramujos"

# }
# # for i in(d):
# #     print(i," = ",d.get(i))

# # 02. Usando o dicionário d criado anteriormente, imprima seu nome;
# print(d["nome"])

# # 03. Crie um dicionário dict e coloque nele os dados fornecidos pelo usuário: nome, idade, telefone, endereço;
# d={


# }

# nome_usuario = input("Digite seu nome: ")
# d.update({"nome":nome_usuario})
# idade_usuario = input("Digite sua idade: ")
# d.update({"idade":idade_usuario})
# telefone_usuario = input("Digite seu telefone: ")
# d.update({"telefone":telefone_usuario})
# endereco_usuario = input("Digite seu endereço: ")
# d.update({"endereço":endereco_usuario})

# # 04. Também usando dict, imprima todos os itens do dicionário no formato chave : valor;
# for i in(d):
#     print(i," = ",d.get(i))

# # 05. Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário. 
# #     Leia os dados (nome, telefone) de todos os contatos do usuário de forma que a agenda fique completa, imprima todos os contatos e por fim, 
# #     faça uma pesquisa pelo nome e apresente o telefone.
# agenda={

# }
# quantidadeDeContatos = int(input("Digite quantos contatos você deseja salvar: "))

# for i in range(quantidadeDeContatos):
#     nome=input(f"digite o {i+1}° nome:")
#     telefone=input(f"digite o {i+1}° telefone:")
#     agenda.update({nome:telefone})

# for i in(agenda):
#     print(i," = ",agenda.get(i))

# contato=input("Qual contato você gostaria de conferir? ")
# if contato in agenda:
#     print(f"{contato}"," = ",agenda.get(contato))
# else:
#     print("Contato não encontrado")

# # 06. Crie um programa que armazena um grupo de 3 pessoas contendo o número de telefone de cada uma, a idade de cada uma, depois mostre todas as informações 
# #e a informação apenas de uma pessoa. 

# grupo={}

# for i in range(3):
#     nome=input(f"Digite o {i+1}° nome:")
#     telefone=input(f"Digete o {i+1} telefone:")
#     idade=input(f"Digte a {i+1}°")

#     grupo.update({nome:(telefone,idade)})

# for i in grupo:
#     print(i," = ", "telefone:",grupo.get(i)[0],", ","idade:",grupo.get(i)[1])

# 07. Faça um programa que carregue um dicionário com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
#O dicionário deve armazenar quantos quilômetros cada um desses carros faz com um litro de combustível e o nome do veículo. 
# Calcule e mostre:
# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 5,25 o litro. 
# Abaixo segue uma tela de exemplo. 
# O disposição das informações deve ser o mais próxima possível ao exemplo. 
# Os dados são fictícios e podem mudar a cada execução do programa.
# Veículo 1
# Nome: fusca
# Km por litro: 7
carros={}

for i in range(2):
    modelo=input(f"Digite o modelo do {i+1}° carro:")
    consumo=float(input(f"Digite o consumo do {i+1}° veículo em km/l:"))
    carros[f"veiculo{i+1}"]= {
        "modelo":modelo,
        "consumo":consumo
    }

maior=0
for i in carros:
    if carros.get(i)["consumo"]>maior:
        maior = carros.get(i)["consumo"]
        modelo=carros.get(i)["modelo"]
print(modelo,"-",maior, " km/l")


for i in carros







    





