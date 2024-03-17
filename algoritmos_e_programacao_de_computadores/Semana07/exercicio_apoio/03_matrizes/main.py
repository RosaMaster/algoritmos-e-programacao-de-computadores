# Exercício 03: Matrizes
# Dev: RosaMaster
# Título: Matrizes
# Descrição: Escreva uma função soma2D() que aceita duas listas bidimensionais do mesmo
# tamanho (ou seja, o mesmo número de linhas e colunas) como argumentos de entrada e
# incrementa cada entrada na primeira lista com o valor da entrada correspondente
# na segunda lista.
#        
# >>> t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
# >>> s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
# >>> soma2D(t,s)
# >>> for linha in t:
# print(linha)
#
# [4, 8, 4, 5]
# [5, 2, 10, 3]
# [8, 4, 6, 6]

def soma2D(t, s):
    for i in range(len(t)):
        for j in range(len(t[i])):
            t[i][j] += s[i][j]
    for linha in t:
        print(linha)

t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
soma2D(t, s)

