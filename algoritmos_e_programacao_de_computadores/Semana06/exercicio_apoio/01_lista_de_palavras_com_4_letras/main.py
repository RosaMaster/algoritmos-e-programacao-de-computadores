# Exercício 01: Lista de Palavras com 4 Letras
# Dev: RosaMaster
# Título: Lista de Palavras com 4 Letras
# Descrição: Implemente um programa que solicite do usuário uma lista de palavras
# (ou seja, strings) e depois exiba na tela, uma por linha, todas as strings de
# quatro letras nessa lista.

# >>>
# Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote']
# pare pote


def lista_palavras(lista_palavras):
    """ Função responsável por exibir as palavras com 4 letras.

    Args:
        lista_palavras (list): lista de palavras
    """
    for palavra in lista_palavras:
        if len(palavra) == 4:
            print(palavra, end=' ')


palavras = []
for i in range(4):
    palavra = input('Digite a palavra: ')
    palavras.append(palavra)

print(palavras)

lista_palavras(palavras)

