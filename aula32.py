a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

# a inserção de indices dentro das chaves ajuda na hora em que vc quer repetir o format
# nome1=a é um parâmetro nomeado. tudo o que vem depois dele, tem que vir nomeado tbm
# caso nomeasse somente o c, não necessitaria nomear o a e o b, pois só tem que nomear do argumento
# para frente
