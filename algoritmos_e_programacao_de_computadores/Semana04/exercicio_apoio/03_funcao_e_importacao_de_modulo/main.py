# Exercício 03: Função e Importação de Módulo
# Dev: RosaMaster
# Título: Função e Importação de Módulo
# Descrição: Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo
# (um número não negativo) e retorna o perímetro do círculo. Você deverá escrever sua
# implementação em um módulo chamado perímetro.py. Um exemplo de uso é:
#
# >>> perimeter(1)
# 6.283185307179586

# Entrada
import math

def perimeter(radius):
    return 2 * math.pi * radius

# Teste
print(perimeter(1))
print(perimeter(2))
print(perimeter(3))
print(perimeter(4))
print(perimeter(5))

