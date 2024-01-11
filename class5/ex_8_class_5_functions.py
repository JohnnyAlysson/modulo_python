# 8. Construa um programa que leia um caractere (letra) e, por meio de uma
# função, retorne se este caractere é uma consoante ou uma vogal. Ao final imprima
# o resultado.

#Definir função
    #Função recebe um caractere se o caractere for vogal, retorna vogal, caso contrário retorna consoante
def vowelOrConsonant(character):
    vowels = ("a","e","i","o","u")
    if character in vowels:
        return f"The character {character} is a vowel"
    else:
        return f"The Character {character} is a consonant"
#Solicitar do usuário 1 letra e fazer a validação
user_char=input("Type a letter: ")
    
#imprimir resultado chamando a função
print(vowelOrConsonant(user_char))

