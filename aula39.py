# Operadores lógicos 
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,  a expressão inteira será avaliada naquele valor.
# São considerados falsy (que você já viu)
# 0 0.0 '' False 
# Também existem o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')    
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E'  or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')

# Primeiro será verificado os parênteses. Neste caso, será verificado se a letra digitada
# é um 'e' minusculo ou um 'E'. Caso seja verdadeira, ele irá
# checar a segunda condição. Se ambas forem verdadeiras, então ele entra na condição do if
# Caso uma das duas seja falsa,  ele já vai para o else

else:
    print('Sair')

# Avaliação de curto circuito
print(0 or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha) 