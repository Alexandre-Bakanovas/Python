"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Creat Read Update Delete (CRUD)
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# lista[2] = 300

# del lista[2] #Aqui ele vai apagar o índice 2 da lista, que era o 300. A partir dai, o python reor-
# ganiza o resto da lista, então o novo índice 2 passa a ser o 40
# Fazer com que o python fique movendo os dados dentro da lista faz com que o programa fique
# lento, por isso é interessante remover do final e inserir no final. Isso quando a lista é grande
# print(lista)
# print(lista[2])

lista.append(50) #Método para adicionar um novo valor à lista.
print(lista)

# ultimo_valor = lista.pop() - remove o último ítem da lista. Mas, se passar um valor a ele,
# ele remove o índice passado

removido = lista.pop(3)

print(lista, 'Valor removido: ', removido)