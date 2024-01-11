# 6. Faça um programa que verifique se um número é primo por meio de um função.
# Ao final imprima o resultado.



def checkNumberPrime(number):
    for i in range(2,number):
        if number % i == 0 or number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
            print(f" Número {number} não é primo")
            break
        else:
            print(f" Número {number} é primo")
            break
    
    

number= int(input("Digite um número:"))

checkNumberPrime(number)
