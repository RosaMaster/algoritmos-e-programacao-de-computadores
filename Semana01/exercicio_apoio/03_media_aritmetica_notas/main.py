# Exercício 03: Média Aritmética Notas
# Dev: RosaMaster
# Título: Média Aritmética Notas
# Objetivo: Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno
# representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética
# (variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a
# média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno
# Reprovado com média”. Informar também, após a apresentação das mensagens, o valor
# da média obtida pelo aluno.

# Notas
N1 = float(input('Digite a nota 1: '))
N2 = float(input('Digite a nota 2: '))
N3 = float(input('Digite a nota 3: '))
N4 = float(input('Digite a nota 4: '))

# Média
MD = (N1 + N2 + N3 + N4) / 4

# Verificação
if MD >= 5:
    print('Aluno Aprovado com média', MD)
else:
    print('Aluno Reprovado com média', MD)


# Fim
    
