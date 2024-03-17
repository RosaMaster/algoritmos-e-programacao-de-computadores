# Exercício 05: Escrevendo Expressões
# Dev: RosaMaster
# Título: Escrevendo Expressões
# Descrição: Escreva expressões Python correspondentes ao seguinte:
#
# O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados
# têm comprimentos a e b
# O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
# A área de um disco com raio a
# O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está
# dentro de um círculo com centro ( a, b ) e raio r

# Expressão 1
a = 3
b = 4
hipotesenusa = (a**2 + b**2)**0.5
print(hipotesenusa)

# Expressão 2
print(hipotesenusa == 5)

# Expressão 3
raio = 3
area = 3.14 * raio**2
print(area)

# Expressão 4
x = 2
y = 3
a = 0
b = 0
r = 5
dentro = (x - a)**2 + (y - b)**2 < r**2
print(dentro)

# fim



