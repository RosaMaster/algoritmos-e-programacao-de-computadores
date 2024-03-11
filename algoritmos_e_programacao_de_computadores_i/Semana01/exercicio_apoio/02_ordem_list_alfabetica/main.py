# Exercício 02: Lista de palavras
# Dev: RosaMaster
# Título: Ordem Lista Alfabetica
# Objetivo: Primeiro, execute a atribuição palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
# Agora, escreva duas expressões Python que são avaliadas, respectivamente, como a primeira e a última palavras em palavras, na ordem do dicionário.
# Em seguida, escreva uma expressão Python que ordene a lista.

# Lista de palavras
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']

first = palavras[0]
last = palavras[-1]

print(palavras[0] + ' ' + palavras[-1])
print(type(palavras)) # <class 'list'>
print(first + ' ' + last)

palavras.sort()

# print lista ordenada
print(palavras)

