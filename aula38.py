# Operador lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele Valor 
# São considerador falsy (que você já viu)
# 0 0.0 '' false 
# Também existe o tipo None que é usado para representar um não Valor 

entrada = input('[E]ntrar [S]air: ')    
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')

# Primeiro será verificado se a primeira condição é verdadeira. Caso seja verdadeira, ele irá
# checar a segunda condição. Se ambas forem verdadeiras, então ele entra na condição do if
# Caso uma das duas seja falsa,  ele já vai para o else

else:
    print('Sair')

# Avaliação de curto circuito
print(True and True and True)
print(True and 0.0 and True)