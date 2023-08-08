"""
Introdução ao desempacotamento e empacotamento.
"""

nomes = ['Maria', 'Helena', 'Luiz']

# nome1, nome2, nome3 = nomes #isso faz com que cada um dos dados da lista entre respectivamente 
# dentro das variaveis colocadas a esquerda.

nome_1, *resto = nomes

# Por convenção,os desenvolvedores utilizam o "_" para poder ignorar os valores.

# _, nome_2, _ = ['Maria', 'Helena', 'Luiz'] - Modelo

print(nome_1, resto)
