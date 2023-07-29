# if / elif        / else
# se   / se não se   / se não
# Aula para aprender if, elif e else

entrada = input('Você quer "entar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair':
    print('Você saiu do sistema.')
else:
    print('Você não digitou nem entrar ou sair.')

print('Fora dos blocos')

# Posso ter um if sozinho, um if e um elif, ou um if e um else, mas unca um elif e um else
# Quando o interpretador do python encontra algo versdadeiro dentro das condições, ele executa ele 
# e pula todo o resto

