# Exercício 07: Mapping
# Dev: RosaMaster
# Título: Mapping
# Descrição: Suponha que uma lista não vazia time foi atribuída. Escreva uma instrução Python ou
# instruções que mapeiam o primeiro e último valor da lista. Assim, se a lista
# original for:

# >>> time = [’Ava’, ’Eleanor’, ’Clare’, ’Sarah’]
  
# então a lista resultante deverá ser:
  
# >>> time
# [’Sarah’, ’Eleanor’, ’Clare’, ’Ava’]

time = ['Ava', 'Eleanor', 'Clare', 'Sarah']
time = time[::-1]
print(time) 

# output:
# ['Sarah', 'Clare', 'Eleanor', 'Ava']



