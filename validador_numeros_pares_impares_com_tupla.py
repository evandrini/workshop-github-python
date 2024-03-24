lista_valores = []
numeros = 0

while True:
    user_valor = int(input("Digite um valor inteiro: "))
    numeros += 1
    lista_valores.append(user_valor)

    if numeros == 10:
        break

print("Valores digitados:", lista_valores)

pares = []
impares = []

for numeros in lista_valores:
    if numeros % 2 == 0:
        pares.append(numeros)
    
    else:
        impares.append(numeros)

print("Números pares:", pares)
print("Números ímpares:", tuple(impares))
print("Quantidade de números pares:", len(pares))
print("Quantidade de números ímpares:", len(impares))
print("Soma dos números pares:", sum(pares))
print("Soma dos números ímpares:", sum(impares))
