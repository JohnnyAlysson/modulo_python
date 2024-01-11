# PROJETO FUNÇÕES
# Escreva um programa para armazenar uma agenda de telefones em um dicionário. O programa deve oferecer uma lista de opções ao usuário até que o mesmo deseje encerrar, 
# e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções: 
# incluirContato - essa função acrescenta um novo nome na agenda. Ela deve receber como argumentos o nome e o telefone. A função deve emitir uma mensagem de sucesso ou erro. 
# alterarContato - essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-lo. 
# Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome.. A função deve emitir uma mensagem de sucesso ou erro.
# excluirContato - essa função exclui um contato que já está na agenda. A função deve emitir uma mensagem de sucesso ou erro.
# consultarContato - essa função busca na agenda um contato por meio do nome informado. 
# consultarContatos - essa função retorna os contatos da agenda, caso a mesma não esteja vazia.
# limparContatos - essa função deve limpar a agenda.

#1. create dictionary to store the contacts
contact_list={}
#2. create fuctions for each  option
    #2.1 Add contact incluirContato
def incluirContato(nome,telefone):
    if nome in contact_list:
        print("\nContato já existe, não foi possivel inclui-lo")
    else:
        contact_list[nome] = telefone
        print("\nContato Cadastrado com sucesso!")
    #2.2 change contact alterarContato
def alterarContato(nome, telefone):
    if nome in contact_list:
        contact_list[nome] = telefone
        print("\nNúmero Cadastrado com sucesso!")
    else:
        user_input = input("\nNome não encontrado na lista, Você gostarria de inclui-lo?\n S - Sim ou N- não?").lower()
        if user_input == "s" or user_input == "sim":
           contact_list[nome] = telefone 
           print("\nNúmero Cadastrado com sucesso!")
    #2.3 delete contact excluir Contato
def excluirContato(nome):
    if nome in contact_list:
        contact_list.pop(nome)
        print("\nContato excluido com sucesso!")
    else:
        print("\nNome não encontrado na sua lista de contatos")
    #2.4 check by name consultarContato
def consultarContato(nome):
    if nome in  contact_list:
        print(f"\n Nome: {nome}\n Número: {contact_list.get(nome)}")
    else:
        print("\nNome não encontrado na sua lista de contatos")
    #2.5 show contact list consultarContatos
def consultarContatos():
    count = 1
    for contact in contact_list:
        print(f"*"*30)
        print(f"{count}° contato:")
        print(f" Nome : {contact}, Número : {contact_list.get(contact)}")
        count +=1
    #2.6 clean contact list limparContatos
def limparContatos():
    contact_list.clear()
#3. loop while with the options
print("Bem vindo a sua Agenda:")   
while True:
    user_choice = input('''
    Qual ação você gostaria de realizar?
        1 - Incluir novo contato
        2 - Alterar contato
        3 - Excluir contato
        4 - Consultar um contato
        5 - Consultar todos os contatos
        6 - Limpar lista de contatos
        7 - Sair.
        ''').lower()
    if user_choice == "1" or user_choice == "incluir novo contato":
        nome_contato = input(" Digite o nome do contato:").title()
        numero_contato = input(" Digite o número:")
        incluirContato(nome_contato,numero_contato)

    elif user_choice == "2" or user_choice == "alterar contato":
        nome_contato = input(" Digite o nome do contato:").title()
        numero_contato = input(" Digite o número:")
        alterarContato(nome_contato,numero_contato)

    elif user_choice == "3" or user_choice == "excluir contato":
        nome_contato = input(" Digite o nome do contato:").title()
        excluirContato(nome_contato)

    elif user_choice == "4" or user_choice == "consultar um contato":
        nome_contato = input(" Digite o nome do contato:").title()
        consultarContato(nome_contato)

    elif user_choice == "5" or user_choice == "consultar todos os contatos":
        consultarContatos()
    elif user_choice == "6" or user_choice == "limpar lista de contatos":
        limparContatos()
    elif user_choice == "7" or user_choice == "sair":
        print(" Encerrando...")
        break
    else:
        print("Comando inválido digite novamente")

