"""
*Criar variaveis para nome (str), idade (int)
*altura (float) e peso (float) de uma pessoa
*Obter o ano de nascimento da pessoa
*Obter o IMC da pessoa com 2 casas decimais
* Exibir um texto com todos valores na tela usando F-string (com as chaves)
"""
nome = 'Tiago Pimenta'
idade = 18
altura = 1.65
peso = 45.5
ano_atual = 2021
nascimento = ano_atual - idade
Imc= 45.5 // (1.65 * 1.65 )
print(f'{nome} tem {idade}, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {Imc:.2f}')
print('{} nasceu em {}'.format(nome, nascimento))