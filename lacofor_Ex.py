soma=0
max_idade=0
contador_menor_20=0

for variavel in range (0,3):
    nome = str(input("Digite seu nome:"))
    idade = int(input("Digite sua idade:"))
    sexo = str(input("Digite M (Masculino ou F(Feminino):"))
    soma = soma + idade
            
    if idade >= max_idade:
        print("Encontramos a maior idade!")
        idade = max_idade
        nome_max_idade = nome

    if (idade<20):
        contador_menor_20 = contador_menor_20 +1
        
media = soma/3
print(f"A média de idade é:", {media})
print(f"A maior idade é {max_idade} da pessoa {nome_max_idade}")
print(f"Total de pessoas menor que 20 anos é", {contador_menor_20})