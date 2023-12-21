# #Dada uma tupla T de n valores inteiros, escreva um programa que remova todos os números pares da tupla.
# tupla = ()
# contador = int(input("Quantos números a tupla possui?"))#contador
# lista = list(tupla)


# for i in range(contador):
#     numero=input(f"Digite o {i+1}° número:")
#     lista.append(numero)
# for i in lista:
#     if int(i)%2 == 0:
#         lista.remove(i)
# tupla=tuple(lista)

# print(lista)


# # Dadas duas tuplas P1 e P2, ambas com n valores reais que representam as notas de uma turma na prova 1 e na prova 2, respectivamente, 
# # # escreva um programa que calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a turma obteve a melhor média.
# p1=()
# p2=()
# contador=int(input("Quantos alunos a turma possui? ")) #contador
# lista1 = list(p1)
# lista2 = list(p2)

# for i in range(contador):
#     nota1=int(input(f"Digite a {i+1}° nota da primeira prova:"))
#     lista1.append(nota1)
#     nota2=int(input(f"Digite a {i+1}° nota da segunda prova:"))
#     lista2.append(nota2)

# media1= sum(lista1)/contador
# media2= sum(lista2)/contador

# print(f"Média prova 1: {media1/contador}")
# print(f"Média prova 2: {media2/contador}")

# if media1 >media2:
#     print("A turma foi melhor na prova 1")
# if media2 < media1:
#     print("A turma foi melhor na prova 2")
# else:
#     print("As médias são iguais")

# # Dadas duas tuplas L1 e L2, com n e m valores inteiros, respectivamente, escreva um programa que concatene as tuplas L1 e L2 em uma nova tupla L3.
# # Em seguida, imprima a tupla L3 ordenada de maneira crescente e decrescente.
# l1=()
# l2=()
# contador1 = int(input("Quantos números a tupla 1 possui? "))
# contador2 = int(input("Quantos números a tupla 2 possui? "))
# lista1 = list(l1)
# lista2 = list(l2)

# for i in range(contador1):
#     n1=int(input(f"Digite o {i+1}° número:"))
#     lista1.append(n1)

# for i in range(contador2):
#     n2=int(input(f"Digite o {i+1}° número:"))
#     lista1.append(n2)

# l3=lista1+lista2
# l3.sort()

# print(tuple(l3))   

