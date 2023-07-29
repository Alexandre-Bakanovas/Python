"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'luiz Otávio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC' #Não é possível realizar essa operação pois ele é imutavel!!!
print(string.zfill(100))
print(outra_variavel)

