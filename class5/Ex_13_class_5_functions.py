# 4.Crie Funções para calcular de acordo com os operadores matemáticos de uma calculadora:
# ●somar(parm1, parm2) 
# ●subtracao(parm1, parm2) 
# ●multiplicacao(parm1, parm2) 
# ●divisao(parm1, parm2)
# o programa deve receber dois números inteiros ou float e possa calcular esses números de acor do com a escolha dos usuários sob operadores. 
# Use um laço de repetição infinito e verifique a cada resultado da operação selecionada se o usuário deseja continuar calculando, 
# se não, interrompa o loop e finalize o programa. use bloco condicional para chamar a função apropriada 
# a função de divisão deverá informar ao usuário uma mensagem de erro se o divisor for igual a zero


#definir 4 funções com impressões proprias:
    #soma:
def sum(number_1,number_2):
    return number_1+number_2
    #subtração:
def subtraction(number_1,number_2):
    return number_1-number_2
    #divisão:
def division(number_1,number_2):
    if number_2 == 0:
        number_2 = input("Please, put a number higher than 0: " )
    return number_1/number_2
    #mult:
def multiplication(number_1,number_2):
    return number_1*number_2

#solicitar do usuário 2 números:
user_number1= float(input("Type the first number: "))
user_number2= float(input("Type te second number: "))
#laço while com as 4 opções anterirores e end:
user_choice= 0
while True:
    user_choice= input("What operation do you want?\n    1. Sum\n    2. Subtraction\n    3. Division\n    4. Multiplication\n    5. End:\n")
    if user_choice == '1' or user_choice ==  "Sum":
        print(sum(user_number1,user_number2))
    elif user_choice == '2' or user_choice ==  "Subratraction":
        print(subtraction(user_number1,user_number2))
    elif user_choice == '3' or user_choice ==  "Division":
        print(division(user_number1,user_number2))
    elif user_choice == '4' or user_choice ==  "Multiplication":
        print(multiplication(user_number1,user_number2))   
    elif user_choice == "end" or user_choice == "5":
        print("program End")
        break
    else:
        print("Invalid input, try again")

