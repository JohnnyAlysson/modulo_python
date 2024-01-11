## Exercises about Lambda function ###
 # 1. Escreva uma função lambda que receba um número e verifique se ele é par ou ímpar. 
# A função deve retornar "par" se o número for par e "ímpar" caso contrário. 
EvenOrOdd = lambda x: f"The number {x} is Even" if x % 2 ==0 else f" the number {x} is Odd"
user_number = int(input("What number do you want to check? "))
print(EvenOrOdd(user_number))

# 2. Implemente uma função lambda que receba duas strings e retorne a concatenação das duas, 
# apenas se ambas as strings tiverem mais de 5 caracteres. Caso contrário, a função deve retornar uma mensagem de erro.
Concatenate_string = lambda firstword,secondword : firstword+secondword
user_word1 = input("What is the first word? ")
user_word2 = input("What is the second word? ")
print(Concatenate_string(user_word1,user_word2))

# 3. Escreva uma função lambda que receba um número e verifique se ele é maior que 10. Se for maior, 
# a função deve retornar o próprio número; caso contrário, deve retornar o número dividido por 2. 
CheckNumber= lambda x: x if x<10 else x/2
user_num= float(input("What's the number? "))
print(CheckNumber(user_num))

# 4. Implemente uma função lambda que receba um número e verifique se ele é divisível por 3 e por 5. 
# A função deve retornar "divisível" se a condição for satisfeita e "não divisível" caso contrário.
Divisible = lambda number: "Divisible" if number % 3==0 and number%5==0 else "Not divisible"
user_choice = int(input("Type a number to check: "))
print(Divisible(user_choice))