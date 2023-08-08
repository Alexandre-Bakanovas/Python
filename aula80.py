"""
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, celar, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)
# lista = list()
# lista = [] #Aqui ela está vazia
# print(bool(lista)) - Gera um valor falso pois a lista esta vazia
# print(lista, type(lista))


# Acessando o ítem inteiro de cada lista:
#       +0      1          2         3    4
#       -5    -4           -3      -2   -1
lista = [123, True, 'Luiz Otávio', 1.2, []]
print(lista)
lista[-3] = 'Maria' #Alteração do valor da lista 
print(lista[2])
print(lista)


