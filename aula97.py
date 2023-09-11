"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""

# print('Valor' if True else 'Outro valor')
# condicao = 10 == 10
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

digito = 9 # Se ele for maior que 9, ele será 0
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)


a = 0
b = 3
c = 0
d = 0
e = 0
for i in range(50, 20, -2):
    a = (i/2) + 3
    b = b + i
    b = b + 10
    c = a + 13
    d = (i - 1) * 2 * 13
    print(a,b,c,d)