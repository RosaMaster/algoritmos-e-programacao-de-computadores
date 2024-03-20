# Iremos depurar o programa ao lado utilizando o depurador. O programa gera um erro durante sua execução. 

# Função H: Recebe um número n e imprime 1/n e n.
def h(n):
    print('Start h')
    print(n)
    print(1/n)
    #print(n)

# Função G: Recebe um número n e chama a função h com n-1 e imprime n.
def g(n):
    print('Start g')
    print(n)
    h(n-1)
    #print(n)

# Função F: Recebe um número n e chama a função g com n-1 e imprime n.
def f(n):
    print('Start f')
    print(n)
    g(n-1)
    #print(n)

# Chamada da função f com o valor 2.
f(4)

