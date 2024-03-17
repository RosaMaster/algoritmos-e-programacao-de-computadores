# Exercício 01: Conversor de Temperatura II
# Dev: RosaMaster
# Título: Conversor de Temperatura II
# Descrição: Implemente um programa que solicita a temperatura atual em graus Fahrenheit
# do usuário e exibe a temperatura em graus Celsius usando a fórmula:

# A fórmula de conversão é F ← C * 9 / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

# Entrada
print('Conversor de temperatura de graus Fahrenheit para graus Celsius')
fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))

# Processamento
celsius = (fahrenheit - 32 ) * 5 / 9


# Saída
print(f'{fahrenheit} °F é equivalente a {celsius} °C')

# Teste
# 32°F é equivalente a 0°C
# 212°F é equivalente a 100°C
# 98.6°F é equivalente a 37°C
# 77°F é equivalente a 25°C
# 50°F é equivalente a 10°C
# 59°F é equivalente a 15°C
# 68°F é equivalente a 20°C
# 86°F é equivalente a 30°C
