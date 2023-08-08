# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0         1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0        1          2
    ['Luiz', 'João', 'Eduarda', ], # 2
]

# primeiro, b, *_, ultimo = lista
# print(primeiro, ultimo)

# for nome in lista:
#     print(nome, end=' ') é igual a fazer o que está embaixo:
# print(*lista)

# Também é possível fazer esse desempacotamento com strings e tuplas:

# print(*string)
# print(*tupla)

print(*salas, sep='\n')
