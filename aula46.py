"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i - inicio / f - fim / passo - de quanto em quanto caracteres ele vai andar
sempre que quiser pegar um a mais, tem que colocar um a mais pois o indicie finaç não é incluido
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
print(variavel[-1:-10:-1])
print(len(variavel))

