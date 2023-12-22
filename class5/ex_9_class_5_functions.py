# Faça uma função que retorne o reverso de um número inteiro informado. 
# Por exemplo: 127 -> 721

#definir função com um argumento
    #Funçao recebe uum número,armazena cada caractere em uma lista, inverte e concatena o novo número
def inverter(intnumber):
    string_number=str(intnumber)
    number_break= []
    for i in string_number:number_break.append(i)
    number_break.reverse()
    new_number = ""
    for i in number_break:
        new_number = new_number + i
    return new_number
# Solicitar input do usuário
user_number= int(input("Type a number"))
#chamar função
print(f"{user_number} >>> {inverter(user_number)}")