"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = enumerate(lista)

# for item in lista_enumerada:
#     print(item) - fazendo dessa forma consumimos o iterator, então não é a melhor coisa

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

for indice, nome in enumerate(lista):
    # indice, nome = item
    print(indice, nome)