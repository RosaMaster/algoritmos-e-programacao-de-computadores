# Exercício 06: Diagrama
# Dev: RosaMaster
# Título: Diagrama
# Descrição: Desenhe um diagrama representando o estado dos nomes e objetos após esta execução:

# >>> a = [5, 6, 7]
# >>> b = a
# >>> a = 3

# Resposta:
# a = 3
# b = [5, 6, 7]

# Explicação: a variável a recebeu o valor 3, e a variável b recebeu a lista [5, 6, 7] que foi atribuída a variável a.
# Quando a variável a recebeu o valor 3, a variável b não foi alterada, pois a variável b recebeu a lista que foi atribuída a variável a, e não a variável a em si.

# Diagrama:
# a = 3
# b = [5, 6, 7]

# Código:
a = [5, 6, 7]
b = a
a = 3
print(f'a = {a}')
print(f'b = {b}')

# Saída:
# a = 3
# b = [5, 6, 7]

# Fim


