# Calculadora com while

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um outro número: ')
    operador = input('Digite um operador (+/-*): ')

    numeros_validos = None

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if len(operador) > 1:
        print('Operador inválido.')
        continue

    print('Realizando a sua conta. Confira abaixo o resultado:')
    if operador == '+':
        print(numero_1 + numero_2)
    elif operador == '-':
         print(numero_1 - numero_2)      
    elif operador == '/':
        print(numero_1 / numero_2)        
    elif operador == '*':
         print(numero_1 * numero_2)       


    sair = input('Quer sair? [s]im:  ').lower().startswith('s')
    
    if sair:
        break