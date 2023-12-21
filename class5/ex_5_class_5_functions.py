# 5.Faça um programa que verifique quantas vezes um número é divisível por outro. A função deve receber dois parâmetros, o dividendo e o divisor. 
# Ao ler o divisor, é importante verificar se ele é menor que o dividendo. Ao final imprima o resultado.


numero_1 = int(input("Digite o dividendo: "))
numero_2 = int(input("Digite o Divisor: "))
while numero_1<numero_2:
    numero_1 = input("Dividendo deve ser maior que o divisor:\n Digite novamente:")
    
count=0
while numero_1%numero_2 !=0:
    count +=1
print(count)