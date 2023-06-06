#encontrar numeros pares entre 1 a 100 e dizer quantos são impares
impar=0
par=0
texto = str(" ")

for variavel in range (1,9):
    if (variavel%5) == 0:
        par = par +1
        texto = texto + str(f" {variavel}")    
    else:
        print("O número é impar:", variavel)
print(f"São {par} números pares e os pares são{texto}")

    
    