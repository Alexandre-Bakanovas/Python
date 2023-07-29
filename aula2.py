"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas

Caracter de escape é para que o interpretador pule o que será escrito no próximo caracter.

o "r" é utilizado para poder imprimir tudo o que vem dentro das aspas

Um "truque" é utilizar as aspas simples no início e, caso queira utilizar as aspas dentro do texto,
basta utilizar as aspas duplas ou vice e versa.
"""
print(1234)

# Aspas simples
print('Luiz Otávio')
print(1, 'Luiz "Otávio"')

# Aspas duplas
print("Luiz Otávio")
print(2, "Luiz 'Otávio'")

# Escape
print("Luiz \"Otávio\"")

# r
print(r"Luiz \"Otávio\"")