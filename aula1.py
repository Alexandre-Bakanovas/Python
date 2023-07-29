'''
As 3 aspas seguidas não são um comentário, mas sim uma DocString. Elas parecem com comentário
mas não são. Elas vão ser interpretadas e armazenadas na memória, mas não vão ser impressas.

\r\n é a forma como o windows utiliza para poder fazer a quebra de linha, que é o CRLF
que está presente no canto inferior direito aqui do VScode. No Mac e no Linux é diferente (LF)
\n -> LF é o do mac e linux

sep é utilizado para fazer a separação entre o que está sendo impresso na tela. Por default,
o separador do python é o espaço, mas caso queira mudar, basta utilizar o sep='algo aqui dentro'

end é utilizado para fazer a quebra de linha, que por padrão é o \r\n ou somente o \n. Caso
queira utilizar outra coisa no lugar, pode colocar. No entanto, ao invés de ser feito a quabra
da linha, será impresso no lugar o que você colocou e depois irá para a próxima linha. Pode utilizar
o seguinte end='algo\n' -> neste caso, será escrito algo depois do comando e só depois irá ser feito
a quebra da linha.

Python diferencia letras maiuscula de minuscula. Então Print não é igual a print.

Isso tudo refere-se a aula 18 da udemy
'''
print(12, 34, 1011, sep='-', end='')
print(12, 34, 1011, sep='-', end='\n')
print(12, 34, 1011, sep='-', end='\n')
#Print(12, 34, 1011, sep='-', end='\n') gera erro.