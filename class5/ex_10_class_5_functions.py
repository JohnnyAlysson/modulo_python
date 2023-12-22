# # 10. Faça um programa que leia uma lista com tamanho 10 de números inteiros. Após
# # ler, uma função deve criar uma nova lista com base na primeira, mas, a nova
# # lista deve ser ordenada de forma crescente. O programa deve imprimir esta nova
# # lista após a ordenação

# #definir função que recebe uma lista com 10 numeros e ordena-os de forma crescente

def ordenar(numeros:list):
    numeros.sort()
    return
lista = []
for i in range(10):
    numero= input(f"digite o {i+1}° número:")
    lista.append(numero)
ordenar(lista)
print(lista)