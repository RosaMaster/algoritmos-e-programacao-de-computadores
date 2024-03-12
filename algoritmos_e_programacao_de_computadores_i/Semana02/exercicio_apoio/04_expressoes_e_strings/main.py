# Exercício 04: Expressões & Strings
# Dev: RosaMaster
# Título: Expressões & Strings
# Descrição: Comece executando as instruções de atribuição:
#
# Comece executando as instruções de atribuição:
#
# >>> s1 = 'ant'
# >>> s2 = 'bat'
# >>> s3 = 'cod'
#      
# Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de
# avaliar para:  
#
# 'ant bat cod'
# 'ant ant ant ant ant ant ant ant ant ant'
# 'ant bat bat cod cod cod'
# 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
# 'batbatcod batbatcod batbatcod batbatcod batbatcod'

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

expressao1 = s1 + ' ' + s2 + ' ' + s3
print(f'Expressão 1: {expressao1}')

expressao2 = (s1 + ' ') * 10
print(f'Expressão 2: {expressao2}')

expressao3 = (s1 + ' ' + s2 + ' ') * 2 + s3 + ' ' + s3 + ' ' + s3
print(f'Expressão 3: {expressao3}')

expressao4 = (s1 + ' ' + s2 + ' ') * 7
print(f'Expressão 4: {expressao4}')

expressao5 = (s2 + s2 + s3 + ' ') * 5
print(f'Expressão 5: {expressao5}')

# Fim

# Output:
# Expressão 1: ant bat cod
# Expressão 2: ant ant ant ant ant ant ant ant ant ant 
# Expressão 3: ant bat ant bat cod cod cod
# Expressão 4: ant bat ant bat ant bat ant bat ant bat ant bat ant bat
# Expressão 5: batbatcod batbatcod batbatcod batbatcod batbatcod

