# Title: Dados Faker
# Description: Programa que gera dados falsos
# importando a biblioteca faker
from faker import Faker

# criando um objeto da classe Faker
fake = Faker('pt_BR')

# criando um nome falso
# nome = fake.name()
# print(nome)

# endereco = fake.address()
# print(endereco)

# password = fake.password()
# print(password)

def gerar_pessoa():
    nome = fake.name()
    endereco = fake.address()
    password = fake.password()
    idade = fake.random_int(min=0, max=100)
    saldo = fake.random_int(min=0, max=100000)
    cpf = fake.cpf()
    rg = fake.rg()
    prifissao = fake.job()
    email = fake.email()
    print(email)
    print(f"Nome: {nome}\nSaldo Bancário: R$ {saldo:.2f}\nEndereço: {endereco}\nPassword: {password}\nCPF: {cpf}\nRG: {rg}\nIdade: {idade} anos\n")

gerar_pessoa()
