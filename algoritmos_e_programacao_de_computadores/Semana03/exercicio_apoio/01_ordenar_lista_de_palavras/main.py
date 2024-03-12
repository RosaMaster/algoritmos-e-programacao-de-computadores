# Exercício 01: Ordenar Lista de Palavras
# Dev: RosaMaster
# Título: Ordenar Lista de Palavras
# Descrição: Primeiro, execute a atribuição
#
# palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
# Agora, escreva duas expressões Python que são avaliadas, respectivamente,
# como a primeiro e a última palavras em palavras, na ordem do dicionário.

# Lista de palavras
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']

first = palavras[0]
last = palavras[-1]

print(palavras[0] + ' ' + palavras[-1])
print(type(palavras)) # <class 'list'>
print(first + ' ' + last)

palavras.sort()

first = palavras[0]
last = palavras[-1]

# print lista ordenada
print(palavras)
print(palavras[0] + ' ' + palavras[-1])
print(type(palavras)) # <class 'list'>

# Fim

