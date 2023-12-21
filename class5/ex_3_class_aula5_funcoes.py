#Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto. 
#Faça um programa que permita entrar com o valor de um produto e o percentual de desconto e imprimir o novo valor com base no percentual informado. 
#Para fazer o cálculo, implemente uma função. 

# Definir função:
    #função recebe 2 argumentos, valor do produto e desconto e calcula o seu desconto e mostra o resultado
def calc_price(price,discount):
    new_price= price - (price*(discount/100))
    return new_price
#solicitar do usuário valor do produto e desconto
user_price=float(input("What's the price of the product: "))
user_discount=int(input("What's the discount: "))
#chamar a função com um print
print(f"The new price is: {calc_price(user_price,user_discount)}")

#Faça um programa que leia o saldo e o % de reajuste de uma aplicação financeira e imprimir o novo saldo após o reajuste. O cálculo deve ser feito por uma função.
def reajustment(value,reajust):
    new_value= value + (value*(reajust/100))
    return new_value

user_value=float(input("What's the value: "))
user_reajust=int(input("What's the reajust: "))

print(f"The new value corrected is: {reajustment(user_value,user_reajust)}")