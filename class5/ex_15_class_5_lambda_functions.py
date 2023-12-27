### Exercises about Lambda function ###
from functools import reduce
# 1. A partir de uma lista de strings, utilize map() e uma função lambda para converter todas as letras em maiúsculas. 
names=["johnny", "alysson", "alencar","neves","dos","reis"]
names_caps = list(map(lambda n: n.upper(),names))
print(names_caps)
# 2. A partir de uma lista de palavras, utilize filter() e uma função lambda para filtrar apenas as palavras que possuem mais de 5 letras. 
names=["johnny", "alysson", "alencar","neves","dos","reis"]
name_five_letters = list(filter(lambda n : len(n) >5 ,names))
print(name_five_letters)
# 3. Dada uma lista de valores numéricos, utilize reduce() e uma função lambda para obter o valor máximo da lista. 
numbers = [2,56,7,3,1,8,100,23,89]
max_number= reduce(lambda x,y : x if x > y else y,numbers)
print(max_number)
# 4. A partir de uma lista de dicionários, cada um representando uma pessoa com os campos "nome" e "idade", utilize map() 
# e uma função lambda para obter uma nova lista contendo apenas os nomes das pessoas.
name_n_age ={"johnny":27, "andressa":26, "noah": 2}
names_only= list(map(lambda n: n ,name_n_age.keys()))
print(names_only)
