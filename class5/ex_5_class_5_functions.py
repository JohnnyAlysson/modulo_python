# 5.Faça um programa que verifique quantas vezes um número é divisível por outro. A função deve receber dois parâmetros, o dividendo e o divisor. 
# Ao ler o divisor, é importante verificar se ele é menor que o dividendo. Ao final imprima o resultado.
def division(dividend,divisor):
    count=0
    while dividend//divisor:
        dividend=dividend/divisor
        count +=1
    return count

numero_1 = int(input("Digite o dividendo: "))
numero_2 = int(input("Digite o Divisor: "))
while numero_1<numero_2:
    numero_1 = input("Dividendo deve ser maior que o divisor:\n Digite novamente:")

print(f"O número é divisivel {division(numero_1,numero_2)} vezes")