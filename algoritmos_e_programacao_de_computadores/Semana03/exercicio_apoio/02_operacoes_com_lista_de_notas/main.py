# Exercício 02: Operações com Lista de Notas
# Dev: RosaMaster
# Título: Operações com Lista de Notas
# Descrição: Dada a lista de notas de trabalho de casa dos alunos
#
# >>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# escreva:
# Uma expressão que avalia para o número de 7 notas.
# Uma instrução que muda a última nota para 4.
# Uma expressão que avalia para a nota mais alta.
# Uma instrução que classifica as notas da lista.
# Uma expressão que avalia para a média das notas.

# Lista de notas
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas)

# Uma expressão que avalia para o número de 7 notas.
num_7 = notas.count(7)
print(num_7)

# Uma instrução que muda a última nota para 4.
notas[-1] = 4
print(notas)

# Uma expressão que avalia para a nota mais alta.
nota_mais_alta = max(notas)
print(nota_mais_alta)

# Uma instrução que classifica as notas da lista.
notas.sort()
print(notas)

# Uma expressão que avalia para a média das notas.
media = sum(notas) / len(notas)
print(media)

# Fim

