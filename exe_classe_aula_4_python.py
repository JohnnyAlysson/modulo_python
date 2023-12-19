
## Exercicios slide: ###
# 01. Crie um dicionário d e coloque nele seus dados: nome, idade, telefone, endereço;
d={
    "nome":"johnny",
    "idade":"27",
    "telefone":"8599957543",
    "endereço":"rua dos caramujos"

}
# for i in(d):
#     print(i," = ",d.get(i))

# 02. Usando o dicionário d criado anteriormente, imprima seu nome;
print(d["nome"])

# 03. Crie um dicionário dict e coloque nele os dados fornecidos pelo usuário: nome, idade, telefone, endereço;
d={


}

nome_usuario = input("Digite seu nome: ")
d.update({"nome":nome_usuario})
idade_usuario = input("Digite sua idade: ")
d.update({"idade":idade_usuario})
telefone_usuario = input("Digite seu telefone: ")
d.update({"telefone":telefone_usuario})
endereco_usuario = input("Digite seu endereço: ")
d.update({"endereço":endereco_usuario})

# 04. Também usando dict, imprima todos os itens do dicionário no formato chave : valor;
for i in(d):
    print(i," = ",d.get(i))

# 05. Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário. 
#     Leia os dados (nome, telefone) de todos os contatos do usuário de forma que a agenda fique completa, imprima todos os contatos e por fim, 
#     faça uma pesquisa pelo nome e apresente o telefone.
agenda={

}
quantidadeDeContatos = int(input("Digite quantos contatos você deseja salvar: "))

for i in range(quantidadeDeContatos):
    nome=input(f"digite o {i+1}° nome:")
    telefone=input(f"digite o {i+1}° telefone:")
    agenda.update({nome:telefone})

for i in(agenda):
    print(i," = ",agenda.get(i))

contato=input("Qual contato você gostaria de conferir? ")
if contato in agenda:
    print(f"{contato}"," = ",agenda.get(contato))
else:
    print("Contato não encontrado")

# 06. Crie um programa que armazena um grupo de 3 pessoas contendo o número de telefone de cada uma, a idade de cada uma, depois mostre todas as informações 
#e a informação apenas de uma pessoa. 

grupo={}

for i in range(3):
    nome=input(f"Digite o {i+1}° nome:")
    telefone=input(f"Digete o {i+1} telefone:")
    idade=input(f"Digte a {i+1}°")

    grupo.update({nome:(telefone,idade)})

for i in grupo:
    print(i," = ", "telefone:",grupo.get(i)[0],", ","idade:",grupo.get(i)[1])

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

#Solicitação de dados:
carros={}
for i in range(5):
    modelo=input(f"Digite o modelo do {i+1}° carro:")
    consumo=float(input(f"Digite o consumo do {i+1}° veículo em km/l:"))
    carros[f"Veiculo {i+1}"]= {
        "modelo":modelo,
        "consumo":consumo
    }
#Calculo carro mais econômico:
menor_consumo=0
for i in carros:
    if carros.get(i)["consumo"]>menor_consumo:
        menor_consumo = carros.get(i)["consumo"]
        modelo=carros.get(i)["modelo"]
print(modelo,"-",menor_consumo, "km/l")

print(carros)

maior=0
for i in carros:
    if carros.get(i)["consumo"]>maior:
        maior = carros.get(i)["consumo"]
        modelo=carros.get(i)["modelo"]
print(modelo,"-",maior, " km/l")

# Apresentação de forma ordenada:
for i in carros:
    print(f"    {i}","\n","   Nome: ",carros.get(i)["modelo"],"\n"," Km por litro: ",carros.get(i)["consumo"])

for i in carros:
    calculo_litros = 1000 / int(carros.get(i)[consumo])
    print(f"{carros.get(i)} precisa de {calculo_litros} litros de combustivel para percorrer 1000 km, e custará {calculo_litros * 5.25} ")

# Dado o dicionário acima só efetue a venda e dê baixa no estoque quando a qtde em estoque for maior que a qtde solicitada. 

#Dicionário
estoque = {"tomate": [1000, 2.30],
  			"alface": [500, 0.45],
  		    "batata": [2001, 1.20],
            "feijão": [100, 1.50]}
# imprimir itens, quantidade em estoque e valor
for i in estoque:
    print(i,"\n","Estoque:",estoque.get(i)[0],"\n","Valor:",estoque.get(i)[1])

#Solicitar o item e a qt_desejada
item= input("Digite o item desejado: ")
qt_desejada = int(input("Digite a quantidade desejada: "))

#Checar se a qt desejada é menor que a qt em estoque
    #se qt_solicitada < qt_em_estoque então efetuará a venda mostrando o valor total e dará baixa no estoque atual.
    #Caso contrário programa informa que não possui essa quantidade no estoque e mostra a quantidade atual
    
if qt_desejada < estoque.get(item)[0]:
    print(f"Valor total é : {qt_desejada*estoque.get(item)[1]}\n")
    estoque.get(item)[0]=estoque.get(item)[0]-qt_desejada
else:
    print("Não possuimos quantidade suficiente no estoque")

# novo imprimir itens, quantidade em estoque e valor
for i in estoque:
    print(i,"\n","Estoque:",estoque.get(i)[0],"\n","Valor:",estoque.get(i)[1])

# 09. Faça um programa, utilizando Dicionários , que:
# 1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .
# 2° Passo: Peça para o usuário inserir um número.
# 3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.

caixa_misteriosa= {}
#insersao de dados
for i in range(4):
    posicao= i+1
    coisas= input("coloque alguna coisa aqui: ")
    dados_dicionario={posicao: coisas }
    caixa_misteriosa.update( dados_dicionario)
#inserir um numero

posicao= int(input("Digite um número: "))
#mostrar o que foi inserido na posicao do posicao

if i in caixa_misteriosa.keys():
    print(f"Na posicao {posicao} foi colocada a coisa {caixa_misteriosa.get(posicao)}")
else:
    print("Número não encontrado")    

#10. Faça um programa, utilizando Dicionários , que:
#1° Passo: Peça para o usuário inserir o nome de três funcionários e os mostrar na tela.
#2° Passo: Peça para o usuário demitir um funcionário e mostrar na tela os funcionários restantes.

#criar dicionário
lista_funcionarios={

}
#Adicionar funcinários
for i in range(3):
    nome_funcionario=input(f"Digite do {i+1}° nome de um funcionário: ")
    cargo_funcionario=input(f"Digite o cargo do {i+1}° funcionário :")
    dados_funcionario={nome_funcionario:cargo_funcionario}
    lista_funcionarios.update(dados_funcionario)

#remover funcionário
remocao_funcionario=input("Agora qual funcionário você gostaria de demitir? ")
del lista_funcionarios[remocao_funcionario]

#mostar dicionário com funcionários restantes
print("Nome    >>>    Cargo")
for i in lista_funcionarios:
    print(i, "    >>>    " ,lista_funcionarios.get(i))

    





