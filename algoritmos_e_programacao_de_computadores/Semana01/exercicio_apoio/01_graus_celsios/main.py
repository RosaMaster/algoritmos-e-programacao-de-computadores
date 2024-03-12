# Exercício 01: Conversor de temperatura
# Dev: RosaMaster
# Título: Conversor de temperatura
# Descrição: Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
# A fórmula de conversão é F ← C * 9 / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

# Entrada
print('Conversor de temperatura de graus Celsius para graus Fahrenheit')
celsius = float(input('Digite a temperatura em graus Celsius: '))

# Processamento
fahrenheit = celsius * 9 / 5 + 32

# Saída
print(f'{celsius} °C é equivalente a {fahrenheit} °F')

# Teste
# 0°C é equivalente a 32°F
# 100°C é equivalente a 212°F
# 37°C é equivalente a 98.6°F
# 25°C é equivalente a 77°F
# 10°C é equivalente a 50°F
# 15°C é equivalente a 59°F
# 20°C é equivalente a 68°F
# 30°C é equivalente a 86°F
# 35°C é equivalente a 95°F
# 40°C é equivalente a 104°F
# 45°C é equivalente a 113°F
# 50°C é equivalente a 122°F

