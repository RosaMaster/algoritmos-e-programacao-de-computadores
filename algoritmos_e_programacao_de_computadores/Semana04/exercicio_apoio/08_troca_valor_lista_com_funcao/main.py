# Exercício 08: Troca valor lista com função
# Dev: RosaMaster
# Título: Troca valor lista com função
# Descrição: Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e
# último elementos da lista. Você pode considerar que a lista não estará vazia.
# A função não deverá retornar nada.

# >>> ingredientes = [’farinha’, ’açúcar’, ’manteiga’, ’maçãs’]
# >>> trocaPU(ingredientes)
# >>> ingredientes
# [’maçãs’, ’açúcar’, ’manteiga’, ’farinha’]

def trocaPU(lista):
    lista[0], lista[-1] = lista[-1], lista[0]
    print(lista)

ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
trocaPU(ingredientes)

# output:
# ['maçãs', 'açúcar', 'manteiga', 'farinha']

