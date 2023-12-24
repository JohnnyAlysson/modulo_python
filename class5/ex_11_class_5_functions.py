# 11. Implemente um programa que leia uma mensagem e um caractere. 
# Após a leitura, o programa deve, por meio de função, 
# retirar todas as ocorrências do caractere informado na mensagem colocando * em seu lugar. A função deve também retornar o 
# total de caracteres retirados. Ao final, o programa deve imprimir a frase ajustada e a quantidade de caracteres substituídos.
    #Extra: crie uma função para retornar o número de letras, espaços vazios e quantos sinais de pontuação.  

# Definir função
    # Transformar mensagem em uma lista,
    # Laço for para checar em cada item da lista a ocorrencia do caractere
        # Se tem a ocorrencia, subistitui por "*" e adiciona 1 na contagem
        # Tranformar novamente a lista em uma string
        # Imprimir mensagem alterada e quantidade de caracteres substituidos

import string

def subistituteCharacter(message:str,character:str):
    count=0
    message_list =[]
    for i in message:
        message_list.append(i)
    for i in message_list:
        if i == character:
            position=message_list.index(character)
            message_list.remove(character)
            message_list.insert(position,"*")
            count +=1
    new_message = ""
    for i in message_list:
        new_message = new_message + i
    print(f"\nThe new message is:\n",new_message,f"\nThe character {character} has been removed {count} times") 

def countLetterSpacesNsigns(message):
    count_letter = count_spaces=count_signs=0
    list_signs= string.punctuation 
    for i in message:
        if i.isalpha()==True:
            count_letter +=1
        elif i == " ":
            count_spaces +=1
        elif i in list_signs:
            count_signs +=1
    print(f"Number of letters in this sentences is : {count_letter}",
          "\n",
          f"Number of spaces in this sentense is{count_spaces}"
          "\n",
          f"Number of signs in this sentense is {count_signs}"
          )
          

# Solicitar uma mensagem e um caractere para ser removido
user_message= input("What is the message ?")
user_character=input("what character do you want to substitute: ")

# Chamar função
subistituteCharacter(user_message,user_character)


