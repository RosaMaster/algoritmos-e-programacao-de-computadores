# Exercício 04: Tipo de Objeto
# Dev: RosaMaster
# Título: Tipo de Objeto
# Descrição: Qual é o tipo do objeto ao qual essas expressões são avaliadas?
#
# False + False
# 2 * 3**2.0
# 4 // 2 + 4 % 2
# 2 + 3 == 4 or 5 >= 5

expressao1 = False + False
print(type(expressao1))
print(expressao1)
# output: <class 'int'>

expressao2 = 2 * 3**2.0
print(type(expressao2))
print(expressao2)
# output: <class 'float'>

expressao3 = 4 // 2 + 4 % 2
print(type(expressao3))
print(expressao3)
# output: <class 'int'>

expressao4 = 2 + 3 == 4 or 5 >= 5
print(type(expressao4))
print(expressao4)
# output: <class 'bool'>


# fim

