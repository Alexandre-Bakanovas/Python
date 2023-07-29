nome = input('Qual o seu nome? ')
# o que ele digitar ai, será armazenado na variavel nome, sempre como str
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos número é: {int_numero_1 + int_numero_2}')
# as varias numero_1 e numero_2 são str, então ao se somar elas, será concatenado ao invés de somar
# para resolver isso, deve-se utilizar o método int para transformar os dados em inteiro
# segundo o professor, o melhor a se fazer  é não fazer a transformação toda em uma linha, mas
# sim colocando em uma outra variavel, assim não quebramos o código assim que for digitado algo errado


print(f'O seu nome é {nome=}')
# maneira para se colocar o nome = '...'
