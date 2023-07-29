nome = 'Luiz Otávio'

contador = 0
nova_string = ''
while contador < len(nome):
    nova_string += f'*{nome[contador]}'
    contador += 1

print(nova_string)