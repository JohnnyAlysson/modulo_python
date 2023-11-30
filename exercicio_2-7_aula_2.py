# 2. Ler uma lista de 5 números inteiros e mostre cada número da lista.
i =0
lista=[]
for i in range(5):
    numero=int(input("\n Digite um número inteiro: "))
    lista.append(numero)
print(lista)

# 3. Ler uma lista de 10 números inteiros e mostre-os na ordem inversa(descrescente).
i =0
lista=[]
for i in range(15):
    numero=int(input("\n Digite um número inteiro: "))
    lista.append(numero)
lista.sort()
lista.reverse()
print(lista) 

# 4. Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.
i =0
lista=[]
for i in range(4):
    nota=float(input(f"\n Digite a {i+1}° nota: "))
    while True: #validação do input
        if nota > 10:
            print("Valor inválido")
            nota= float(input("Digite uma nota de 0 a 10:"))
        else:
            break
    lista.append(nota)

print(lista)
print(f"A média das notas é: {sum(lista)/4}")

# 5. Ler uma lista com 20 idades e exibir a maior e menor.
i =0
lista=[]
for i in range(20):
    idade=int(input("\n Digite uma idade: "))
    while True: #validação do input
        if idade < 0 or idade > 120:
            print("Valor inválido")
            idade= int(input("Digite uma idade entre 0 e 120 anos: "))
        else:
            break    
    lista.append(idade)
print(max(lista))
print(min(lista))


# 6. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem numerada.
i =0
lista=[]
for i in range(10):
    letra=input("\n Digite uma letra: ")
    lista.append(letra)
for indice,item in enumerate(lista):
    print(indice + 1,"=",item)

# 7. Ler uma lista de 15 números inteiros e mostre cada número juntamente com a sua posição na lista.
i =0
lista=[]
for i in range(15):
    numero=input("\n Digite um número: ")
    lista.append(numero)

for indice,item in enumerate(lista):
    print(indice + 1,"=",item)






