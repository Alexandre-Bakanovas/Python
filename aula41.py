# Operador in e not int
# Strings são iteráveis - em python significa que podemos navegar item por item
#  0 1 2 3 4 5
#  O t á v i o 
# -6-5-4-3-2-1

nome = 'Otávio'

# print(nome[2]) #Forma utilizada para acessar o iterável desejado.
# print(nome[-4])

print('vio' in nome)
print('á' in nome)
print('z' in nome)
print('-'*10)
print('vio' not in nome)
print('zero' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o  que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')