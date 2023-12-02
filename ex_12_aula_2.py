# 12. Crie um programa que leia 5 números inteiros e os armazene em uma lista de tal forma que todos os números maiores 
# ou iguais que o primeiro fiquem ao lado direito e todos os menores fiquem ao lado esquerdo.

lista=[]
numeros=int(input(f"\nDigite o {1}° número"))
lista.append(numeros)
primeiro=lista[0]
for i in range(4):
    numeros=int(input(f"\nDigite o {i+2}° número"))
    if numeros >= primeiro:
        lista.append(numeros)
    else:
        lista.insert(0,numeros)

print("\n",lista)