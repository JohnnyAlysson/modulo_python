# 11. Crie uma lista com os nomes dos super-heróis que devem participar da Iniciativa Vingadores seguindo a ordem: 
# • Homem de Ferro 
# • Capitão América 
# • Thor 
# • Hulk 
# • Viúva Negra 
# • Gavião Arqueiro
# a. Agora, inclua o Homem-Aranha no final da lista e imprima em qual posição está o Thor.
# b. Infelizmente a Viúva Negra e o Homem de Ferro não fazem mais parte da Iniciativa Vingadores, então retire-os da lista.

vingadores= []
vingadores.extend(["Homem de Ferro","Capitão América","Thor","Hulk","Viúva Negra","Gavião Arqueiro"])
print(vingadores)
vingadores.append("Homem Aranha")
print(vingadores)
print(vingadores.index("Thor"))
vingadores.remove("Viúva Negra")
vingadores.remove("Homem de Ferro")
print(vingadores)