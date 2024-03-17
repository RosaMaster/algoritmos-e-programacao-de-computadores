# Exercício 04: Função e Laço de Repetição FOR
# Dev: RosaMaster
# Título: Função e Laço de Repetição FOR
# Descrição: Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por
# linha, os valores negativos na lista. A função não deverá retornar nada.
#
# >>> negatives([4, 0, −1, −3, 6, −9])
# -1
# -3
# -9

# Entrada
def negatives(lista):
    for i in lista:
        if i < 0:
            print(i)

negatives([4, 0, -1, -3, 6, -9])

# output:
# -1
# -3
# -9