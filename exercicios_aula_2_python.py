


lista = [10,False,85.6,"johnny"]

print (type(lista)) # o programa vai apresentar list
print(lista) 
print(lista[1]) # programa imprime o 2° elemento da lista, pois o indice começa pelo 0
print(len(lista)) # Len indica a quantidade de itens em uma lista
lista[2] = 10.5   # Reatribuindo um novo item a uma posição especificifica na lista
print(lista) 
lista.append("oi") # append adiciona um item novo ao fim da lista
print(lista)

lista = [60,20,40,10,12,2,50]
lista.sort()
print (lista)
lista.reverse()
print(lista)
soma= sum(lista)
print(soma)
print(min(lista))
print(max(lista))

for indices,i in enumerate(lista):
    print(indices + 1 , ">>>" ,i)

lista.insert(3,2)
print(lista)