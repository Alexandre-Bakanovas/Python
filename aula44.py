"""
Interpolação básica  de strings - basicamente a mesma coisa que com format
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço total foi R$ %.2f' % (nome, preco)
print(variavel)

print('O hexadicimal de %d é %08x' % (1500,1500))