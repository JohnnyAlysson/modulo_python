# Considere uma lista de números inteiros 
# Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:
# Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
# Função filter() para obter uma nova lista com números pares da lista numeros
# Função reduce()  para obter a soma de todos os números da lista numeros
# Qual o resultado obtido após a execução das operações acima?

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def quadrado(numero):
    return numero**2

numeros_quadrados = list(map(quadrado,numeros))

print(numeros_quadrados)

def pares(numero):
    if numero%2==0:
        return numero
    
numeros_pares = list(filter(pares,numeros_quadrados))

print(numeros_pares)

resultado_final=reduce(lambda a,b:a+b,numeros_pares)

print(resultado_final)