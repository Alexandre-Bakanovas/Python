"""
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update Delete (CRUD)   
Criar, ler, alterar, apagar, = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1234)
del lista[-1]
# lista.clear() - Limpa a lista
lista.insert(0, 5) #Primeiro argumento é a posição, o segundo argumento é o valor.
print(lista)

# podemos fazer assim tbm lista.insert(1000, 5) - Neste caso, não existe o índice 1000, então o python
# irá fazer o insert no último lugar da lista. O que soa meio errado, mas ele entende que não
# existe o índice 1000 e então coloca no último lugar da lista, que no caso seria o 4