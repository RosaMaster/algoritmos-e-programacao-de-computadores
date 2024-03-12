# Exercício 03: Ordem os Operadores nas Expressões
# Dev: RosaMaster
# Título: Ordem os Operadores nas Expressões
# Descrição: Em que ordem os operadores nas expressões a seguir são avaliados?
#
# 2 + 3 == 4 or a >= 5
# lst[1] * -3 < -10 == 0
# (lst[1] * -3 < -10) in [0, True]
# 2 * 3**2
# 4 / 2 in [1, 2, 3]

RESPOSTA = """
Precedência é a ordem na qual os operadores serão avaliados quando o programa for executado. Em Python, os operadores são avaliados na seguinte ordem:

**

*, /, //, na ordem em que aparecerem na expressão.

%

+ e -, na ordem em que aparecerem na expressão.

comparações na ordem que aparecem

not

and

or

Normalmente essa precedencia para os operadores lógicos é a mais intuitiva, mas na dúvida coloque parenteses.

Cuidado com testar se uma variável esta entre 2 valores

em Matemática 
1
<
�
≤
1
0
1<x≤10

Em Python NÃO podemos escrever

1 < x <= 10
mas temos que escrever assim:

1 < x and x <= 10
"""
