# 7. Faça um programa que leia a base e a altura de um retângulo e imprima o perí-
# metro, a área e a diagonal. Para fazer os cálculos, implemente três funções, cada
# uma deve realizar um cálculo especifico conforme solicitado. Utilize as fórmulas
# a seguir.

# Definir funções com os argumentos de base a altura
    #1º função recebe calcula o perimetro
def perimeter(base,height):
    perimeter = (2*base)+(2*height)
    return perimeter
    #2° função calcula a área
def area(base,height):
    area= base*height
    return area
    #3° função calcula a diagonal
def diagonal(base,height):
    diagonal= ((base**2)+(height**2))**0.5
    return round(diagonal,2)
# Solicitar do usuário a base a altura do retangulo.
measurement_unit=input("What's the measurement unit: ")
user_base= float(input("What's the base lenght: "))
user_height=float(input("What's the height lenght: "))
#chamar as funções em um só print
print(f"This rectangle has a perimeter of {perimeter(user_base,user_height)} {measurement_unit},\n",
      f"an area of {area(user_base,user_height)} {measurement_unit},",
      f"and a diagonal of {diagonal(user_base,user_height)} {measurement_unit}."
      )