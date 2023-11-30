# 8. Faça um programa que armazene 15 números inteiros em um vetor e
# depois permita que o usuário digite um número inteiro para ser buscado no vetor, 
# se for encontrado o programa deve imprimir a posição desse número no vetor, caso contrário,
# deve imprimir a mensagem: "Nao encontrado!".

lista=[]
for i in range(15):
    numero= input("\nDigite um número inteiro: ")
    lista.append(numero)

procura=input("\nAgora, Qual número você deseja procurar? ")

for indice,i in enumerate(lista):
    if procura == i:
        print(f"O número está na posição {indice+1}")
        break

    elif indice == 14:
        print("Número não encontrado")


# 9. Faça um programa que armazene 8 números em uma lista e imprima todos os números. Ao final, imprima o total de números múltiplos de seis.
lista=[]
for i in range(8):
     numero=int(input("Digite digite um número inteiro: " ))
     lista.append(numero)
    
 for i in lista:
     if i % 6 ==0:
         print(i) 
         
# 10. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule e armazene a média. 
# Armazene também a situação do aluno: 1- Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem contendo as notas, a média e a situação de cada aluno.
# Utilize quantas listas forem necessárias para armazenar os dados.

# nomes =[]
# notas_1 =[]
# notas_2 =[]
# medias =[]
# situacões =[]


# for i in range(15):
#     nome=input(f"Digite no nome do {i}° aluno(a)")
#     nota_1=input(f"Digite a nota 1 do {i}° aluno(a)")
#     nota_2=input(f"Digite a nota 2 do {i}° aluno(a)")
#     media=input(f"Digite a nota 1 do {i}° aluno(a)")
#     situacao=input(f"Digite a nota 1 do {i}° aluno(a)")
