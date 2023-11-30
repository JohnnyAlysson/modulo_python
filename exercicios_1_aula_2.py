# 1.Dada a lista abaixo, faça o que se pede:
# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Lista reversa;
# Lista ordenada;
# Acrescente ao final da lista o número 27;
# Exclua o número 9;
# Apague o elemento de posição 10;
# Faça a soma dos elementos;
# Mostre o menor elemento da lista;
# Mostre os número pares;
# Mostre os números ímpares;
# Acrescente os número 89 e 91 após o número 4;
# Finalmente mostre o atual tamanho da lista.

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

lista.reverse()
print(lista)
lista.sort()
print(lista)
lista.append(27)
print(lista)
lista.remove(9)
print(lista)
del lista[10]
print(lista)
soma = sum(lista)
print(soma)
print(min(lista))
print(max(lista))
print(lista)
for i,indice in enumerate(lista):
    print(i, ">>>", indice)

for i in lista:
    if i%2== 0:
        print(i)
for i in lista:
    if i % 2 != 0:
        print(i)
lista.insert(4,91)
lista.insert(4,89)
print(lista)
print(len(lista))


