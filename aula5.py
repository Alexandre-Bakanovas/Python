# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

# Polimorfismo - O sinal de + por exemplo consegue fazer a soma como concatenar
# Não é possível concaternar um str com um int
# Se fosse um javascrip, que é dinâmica e fraca, ela conseguiria resolver o problema acima, 
# mas meio bosta

# Uma string vazia é considerada False e uma string preenchida é considerada True

# aula referente a 22 da udemy

print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')