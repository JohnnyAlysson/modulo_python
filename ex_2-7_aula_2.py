# 2. Ler uma lista de 5 números inteiros #e mostre cada número da lista. 
lista = []

for i in range(5):
    numero= input(f"digite o {i+1}° número:")
    lista.append(numero)
    
print(lista)

#3. Ler uma lista de 10 números inteiros e mostre-os na ordem inversa. 
lista = []

for i in range(10):
    numero= input(f"digite o {i+1}° número:")
    lista.append(numero)
lista.sort()    
lista.reverse()

print(lista)

#4. Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média. 
notas=[]
soma=0

for i in range(4):
    nota=float(input(f"Digite a {i+1}° nota:"))
    while True:
        if nota>10 or nota<0:
            print("Valor Inválido")
            nota=float(input(f"Digite a {i+1}° nota:"))
        else:
            break
    notas.append(nota)
    soma=soma=nota
    
print(notas)
print(soma/4)

#5. Ler uma lista com 20 idades e exibir #a #maior e menor.
idades=[]

for i in range (20):
    idade=int(input(f"Digite a {i+1}° idade:"))
    while True:
        if idade>150 or idade<0:
            print("Valor Inválido")
            idade=int(input(f"Digite a {i+1}° idade:"))
        else:
             break
    idades.append(idade)

print(idades)
maior= max(idades)
menor=min(idades)
print(f"A maior idade é: {maior}")
print(f"A maior idade é: {menor}")

#6. Faça um programa que armazene 10 #letras em uma lista e imprima uma #listagem numerada.
letras=[]

for i in range (10):
    letra=input("Digite uma letra:")
    letras.append(letra)
    
for indice,i in enumerate(letras):
     print(f"{indice+1} 》》》{i}")

#7. Ler uma lista de 15 números inteiros #e mostre cada número juntamente com a #sua posição na lista. 
lista=[]

for i in range(15):
    numero=input(f"Digite o {i+1} número:")
    lista.append(numero)
    
for indice,i in enumerate(lista):
    print(f"{indice+1} 》》》{i}")
    










