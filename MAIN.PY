#lista com 06 nomes:

nomes= ['Aurineide', 'Regiane', 'Thais', 'Michael', 'Brendo' 'Alan']

#usuário informa o índice que deseja alterar
indice = int(input('informe o índice que deseja alterar: '))
indice -= 1

nomes[indice] = input('informe o novo nome: ')

#exibe a lista
for nome in nomes:
    print(nome)