soma=0
for variavel in range(0,6):
    num = int(input(f"Digite o número na posição{variavel}"))
    if (num%2) == 0:
        print("Esse número é par")
        soma = soma + num
    else:
        print("Essa variável é  impar e não entrou na soma!")