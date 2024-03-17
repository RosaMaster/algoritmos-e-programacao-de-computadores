# Exercício 05: Docstring
# Dev: RosaMaster
# Título: Docstring
# Descrição: Acrescente a docstring retorna a média de x e y à função média() e a docstring
# exibe os números negativos contidos na lista lst à função negativos() dos Problemas
# Práticos 3.8 e 3.10. Verifique seu trabalho usando a ferramenta de documentação
# help(). Você deverá receber, por exemplo:

# >>> help(média)
# Ajuda sobre a função média no módulo __main__:
# média(x, y)
#  retorna a média de x e y

def media(a, b):
    """ função calculo media

    Args:
        a (int): first value calculate
        b (int): second value calculate

    Returns:
        float: result function media
    """

    return (a + b) / 2

def negatives(lista):
    """ função que imprimpe os valores dos números negativos presente em lista

    Args:
        lista (list): list of numbers
    """

    for i in lista:
        if i < 0:
            print(i)


help(media)
help(negatives)

