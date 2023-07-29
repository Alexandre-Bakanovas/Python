"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        print('Número digitado é par')
    else:
        print('Número digitado é ímpar')
except:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hora = int(input('Digita um horário: '))
    if hora <= 11:
        print('Bom dia')
    elif hora <= 17:
        print('Boa tarde')
    elif hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Você não digitou um valor de horário compatível.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite o seu primeiro nome: ')
if len(primeiro_nome) <= 4: 
    print('Seu nome é curto')
elif len(primeiro_nome) <= 6: 
    print('Seu nome é normal')
elif len(primeiro_nome) > 6:
    print('Seu nome é muito grande')
