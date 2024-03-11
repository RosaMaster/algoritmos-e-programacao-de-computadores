# Exercício 04: Soma sequencial com laço FOR
# Dev: RosaMaster
# Título: Soma sequencial com laço FOR
# Objetivo: Desenvolver os diagramas de blocos e as codificações em português estruturado usando
# laço incondicional (para) do seguinte problema: Construir um programa que apresente a
# soma dos cem primeiros números naturais (1 + 2 + 3 +...+ 98 + 99 + 100).

# Soma sequencial com laço FOR
soma = 0
for i in range(1, 101):
    
    print(f"valor de i: {i}")
    print(f"valor de soma: {soma}")

    soma += i

    print(soma)

# Fim
    
