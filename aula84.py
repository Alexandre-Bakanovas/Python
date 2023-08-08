"""
Cuidador com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luiz', 'Maria']
# lista_b = lista_a - Neste caso aqui, a lista_b não está copiando o que tem na lista_a, mas sim
# apontando para o mesmo local na memória, ou seja, ambas são a mesma coisa. Modificando uma,
#  modifica a outra

# para apenas copiar, deve utilizar um método:

lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)
