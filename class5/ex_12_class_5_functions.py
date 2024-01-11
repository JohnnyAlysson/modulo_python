# 12. Faça um programa que leia 20 de números inteiros e armazene em uma lista.
# Após essa leitura, o programa deve ler um novo número inteiro para ser buscado
# na lista. Uma função deve verificar se o número lido por último está na lista e
# retornar a posição do número na lista, caso esteja, ou -1, caso não esteja.


# Definir funçao
    #se o número in lista retorna posição,
    #caso contrário retorna -1
def checkNumber(list:list,number):
    if number in list:
        for i in list:
            if number == i:
                position = list.index(i) + 1
                print(f"Number is in the position {position}")
    else:
        print(-1)


# Solicitar do usuário 20 numeros e adiciona-los a uma lista
numbers_list= []
for i in range (5):
    user_number= int(input(f"What's the {i+1}° number: "))
    numbers_list.append(user_number)
number_check=int(input("What number do you want to check?: "))
# Chamar a função
checkNumber(numbers_list,number_check)