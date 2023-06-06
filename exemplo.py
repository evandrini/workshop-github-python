nome = str(input("Digite seu nome:")) #obrigar tipo string
idade = int(input("Digite sua idade:")) #obrigar tipo inteiro


print(nome)
print(idade)

#Tipo de formatação no print com a String

#1º Exemplo
print("Olá {} sua idade é {}".format(nome,idade))

#2º Exemplo
print(f"Olá {nome} sua idade é {idade}")

#ESTRUTURA CONDICIONAL
if idade >= 18:
    print("Você pode entrar na balada!")
else:
    print("Você não pode entrar na balada")