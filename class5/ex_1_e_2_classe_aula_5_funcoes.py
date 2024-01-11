# Class about functions:

# 1.Faça um programa que leia três números e, para cada um, imprimir o dobro. O    cálculo deverá ser realizado por uma função e o resultado impresso ao final do  programa. 
#Definir a função
    #ler 3 numeros e imprimir o dobro deles
print("Program to show the doubles of 3 numbers:\n")
def double(number1,number2,number3):
    print(f"Os dobros são:{number1*2} , {number2*2} e {number3*2}")
#Solicitar do usuário 3 numeros
first_number = int(input("Put the first number:"))
second_number = int(input("Put the second number:"))
third_number = int(input("Put the third number:"))
#chamar a função com os inputs
double(first_number,second_number,third_number)

# 2.Faça um programa que receba as notas de três provas e calcule a média. Para o cálculo, escreva uma função. O programa deve imprimir a média ao final.
#Definir a função
    #ler 3 números soma-los e dividi-los por 3:
def average(grade1,grade2,grade3):
    print(f"The grade average is: {(grade1+grade2+grade3)/3}")
#Solicitar do usuário 3 numeros
first_grade=int(input("Put the first grade"))
second_grade=int(input("Put the second grade"))
third_grade=int(input("Put the third grade"))
#Chamar a função
average(first_grade,second_grade,third_grade)